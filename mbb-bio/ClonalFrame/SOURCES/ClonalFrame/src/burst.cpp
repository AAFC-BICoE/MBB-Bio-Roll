/***************************************************************************
 *   Copyright (C) 2011 by Xavier Didelot   *
 *   xavier.didelot@gmail.com   *
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 *   This program is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU General Public License for more details.                          *
 *                                                                         *
 *   You should have received a copy of the GNU General Public License     *
 *   along with this program; if not, write to the                         *
 *   Free Software Foundation, Inc.,                                       *
 *   59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             *
 ***************************************************************************/
#include "burst.h"

namespace wb {

    Burst::Burst(Alignment * a) {
        data=typize(a);
        /*for (int i=0;i<data->size1;i++) {
        printf("%d\t",i+1);
        for (int j=0;j<data->size2;j++)
            printf("%d\t",gsl_matrix_char_get(data,i,j)+1);
        printf("\n");
    }*/
    }


    Burst::~Burst() {
        gsl_matrix_char_free(data);
    }

    gsl_matrix_char * Burst::typize(Alignment * a) {
        gsl_matrix_char * res;
        //Count number of lcbs
        int lcb=1;
        for (int i=0;i<a->getL();i++)
            if (a->getData(0,i)==UNLINKED)
                lcb++;
        res=gsl_matrix_char_calloc(a->getN(),lcb);
        //Locate beginning and end of lcbs
        int * loclcbs=(int *)calloc(lcb+1,sizeof(int));
        int k=1;
        for (int i=0;i<a->getL();i++)
            if (a->getData(0,i)==UNLINKED)
                loclcbs[k++]=i;
        loclcbs[lcb]=a->getL();

        int * sofar=(int *)calloc(lcb,sizeof(int));
        for (int i=0;i<a->getN();i++)//For each sequence
            for (int j=0;j<lcb;j++) {//For each lcb
            int dejavu=-1;
            for (int k=0;k<sofar[j];k++) {//For each previously seen type of that lcb
                //Find a representant f of this type
                int f=0;
                while (gsl_matrix_char_get(res,f,j)!=k)
                    f++;
                //Test if i and f are the same for the current lcb
                bool equal=true;
                for (int l=loclcbs[j];l<loclcbs[j+1];l++)
                    if (a->getData(i,l)!=a->getData(f,l)) {
                    equal=false;
                    break;
                }
                //If they are, use this type
                if (equal==true) {
                    dejavu=k;
                    break;
                }
            }
            //If the type was not seen before, create a new type
            if (dejavu==-1) {
                gsl_matrix_char_set(res,i,j,sofar[j]);
                sofar[j]++;
            } else {//Otherwise use the preexisting type
                gsl_matrix_char_set(res,i,j,dejavu);
            }
        }
        free(sofar);
        free(loclcbs);
        return res;
    }

    int Burst::diff(int a,int b) {
        int dif=0;
        for (unsigned int loc=0;loc<data->size2;loc++) //Compare each LCB
            if (gsl_matrix_char_get(data,a,loc)!=gsl_matrix_char_get(data,b,loc))
                dif++;
        return dif;
    }

    vector<vector<int> > * Burst::splitGroups() {
        vector<vector<int> > * res=new vector<vector<int> >;
        for (unsigned int i=0;i<data->size1;i++) //For each sequence type
        {
            int slv=-1;
            for (unsigned int j=0;j<res->size();j++) //For each group
                for (unsigned int k=0;k<res->at(j).size();k++) //For each element of the group
                {
                int d=diff(i,res->at(j)[k]);
                if (d<=1) { //If only one LCB is different, we have found a SLV
                    slv=j;
                    goto next;
                }
            }
            next:
            if (slv==-1) {
                //Create a new group
                vector<int> * g=new vector<int>;
                g->push_back(i);//put i in new group
                res->push_back(*g);//add new group to list of groups
            } else
                res->at(slv).push_back(i);//add i to group where an SLV was found
        }

        //Merge groups that can be merged
        rep:
        for (unsigned int i=0;i<res->size();i++)
            for (unsigned int j=i+1;j<res->size();j++)//for all pair of groups (i,j)
                for (unsigned int ii=0;ii<res->at(i).size();ii++)
                    for (unsigned int jj=0;jj<res->at(j).size();jj++)//for all pair of elements (ii,jj) of (i,j)
                        if (diff(res->at(i).at(ii),res->at(j).at(jj))<=1) {//if ii and jj are SLVs or identical
            //merge groups i and j
            for (unsigned int k=0;k<res->at(j).size();k++) res->at(i).push_back(res->at(j).at(k));//add elements of group j into group i
            res->erase(res->begin()+j);//remove group j
            goto rep;//and repeat merging procedure
        }
        return res;
    }

    vector<vector<int> > * Burst::ridDoubles(vector<int> v) {
        vector<vector<int> > * res=new vector<vector<int> >;
        res->push_back(v);
        for (unsigned int i=0;i<res->at(0).size();i++) {
            bool found=false;
            for (unsigned int j=i+1;j<res->at(0).size();j++)
                if (diff(res->at(0)[i],res->at(0)[j])==0) {
                if (found==false) {
                    vector<int> * nv=new vector<int>;
                    res->push_back(*nv);
                    res->back().push_back(res->at(0)[i]);
                    //printf("%d ",res->at(0)[i]);
                }
                res->back().push_back(res->at(0)[j]);
                //printf("%d ",res->at(0)[j]);
                found=true;
                res->at(0).erase(res->at(0).begin()+j);
                j--;
            };
            //printf("\n");
        }
        return res;
    }

    void Burst::burst(Param *p) {
        //Reset the consensus tree of the recorder of p
        delete(p->recorder->consensus);
        Consensus * cons=new Consensus(p,1);
        p->recorder->consensus=cons;
        //Create a new tree
        Tree ** where=p->where;
        Tree * t=p->tree;
        vector<vector<int> > * groups=splitGroups();
        printf("Nb groups=%d\n",groups->size());
        for (unsigned int i=0;i<groups->size();i++)//for each group
        {
            vector<vector<int> > * rid=ridDoubles(groups->at(i));
            vector<vector<int> > * subgroups=sortGroup(rid->at(0));
            //vector<vector<int> > * subgroups=sortGroup(groups->at(i));
            for (unsigned int ii=0;ii<subgroups->size();ii++) {//for each subgroup
                //Put the subgroup together
                for (unsigned int j=1;j<subgroups->at(ii).size();j++)//for each element in each subgroup after the first one
                    t=Tree::move(where[subgroups->at(ii)[j]],where[subgroups->at(ii)[j-1]],0,gsl_vector_char_calloc(p->a->getL()),gsl_vector_char_calloc(p->a->getL()),p);//move it next to the previous element of the group
                Tree * toadd=(where[subgroups->at(ii)[0]])->father;
                //Relocate all redundant types
                for (unsigned int j=1;j<rid->size();j++)
                    for (unsigned int k=1;k<rid->at(j).size();k++)
                        t=Tree::move(where[rid->at(j)[k]],where[rid->at(j)[k-1]],0,gsl_vector_char_calloc(p->a->getL()),gsl_vector_char_calloc(p->a->getL()),p);

                if (subgroups->at(ii).size()==1) {
                    int k;
                    for (k=1;k<rid->size();k++)
                        if (rid->at(k)[0]==subgroups->at(ii)[0]) break;
                    if (k>=rid->size()) continue;
                    toadd=where[subgroups->at(ii)[0]]->father;
                }

                //Add the group to the consensus tree
                if (subgroups->at(ii).size()>0)
                {
                    toadd->age=toadd->n;
                    cons->addNode(toadd);
                }
            }

            //Add the groups of identical sequences
            for (unsigned int j=1;j<rid->size();j++) {
                where[rid->at(j)[0]]->father->age=0;
                //cons->addNode(where[rid->at(j)[0]]->father);
            }
            subgroups->clear();
            rid->clear();
            delete(subgroups);
            delete(rid);
        }
        groups->clear();
        delete(groups);
        t->age=t->n;
        cons->addNode(t);//Also include the root of the tree
        p->tree=t;
        for (int i=0;i<p->a->getN();i++)
            cons->addNode(p->where[i]);//And each leave
    }

    vector<vector<int> > * Burst::sortGroup(vector<int> v) {
        //This vector indicate the father of each ST, or -1 if it is the founder
        gsl_vector_int * fathers=gsl_vector_int_calloc(v.size());
        for (unsigned int i=0;i<v.size();i++)
            gsl_vector_int_set(fathers,i,-1);
        //Create list of slv relationships
        vector<vector<int> > slvs(v.size());
        for (unsigned int i=0;i<v.size();i++)
            for (unsigned int j=i+1;j<v.size();j++)
                if (i!=j && diff(v.at(i),v.at(j))==1) {
            slvs.at(i).push_back(j);
            slvs.at(j).push_back(i);
        }
        //The founder is the st with the most slvs
        int f=0;
        for (unsigned int i=1;i<v.size();i++)
            if (slvs.at(i).size()>slvs.at(f).size())
                f=i;
        //    printf("FOUNDER=%d\n",f);
        //recursively decide on the father of each st
        makeFathers(fathers,&slvs,f);
        gsl_vector_int_set(fathers,f,-1);
        //optimise the father relationships
        optimiseFathers(fathers,&slvs,f);
        //for (int i=0;i<v.size();i++) printf("%d\n",gsl_vector_int_get(fathers,i));
        vector<vector<int> > * res=makeClusters(&v,fathers,f,true);//new vector<vector<int> >;
        //res->push_back(v);
        if (v.size()==2) res->pop_back();//printf("%d\n",res->size());
        return res;
    }

    void Burst::optimiseFathers(gsl_vector_int * fathers,vector<vector<int> > *slvs,int f) {
        for (unsigned int i=0;i<fathers->size;i++)
            if (gsl_vector_int_get(fathers,i)!=-1)//For all non founder
            {
            int current=slvs->at(gsl_vector_int_get(fathers,i)).size();//Number of SLVs of the current father of i
            for (unsigned int j=0;j<slvs->at(i).size();j++) {//For each SLV of i
                int prop=slvs->at(i).at(j);
                if (slvs->at(prop).size()>current && !descended(prop,i,fathers)) {
                    current=slvs->at(prop).size();
                    gsl_vector_int_set(fathers,i,prop);
                };
            }
        }
    }

    bool Burst::descended(int which,int orig,gsl_vector_int * fathers) {
        if (which==orig)
            return true;
        for (unsigned int i=0;i<fathers->size;i++)
            if (gsl_vector_int_get(fathers,i)==orig && descended(which,i,fathers))
                return true;
        return false;
    }

    void Burst::makeFathers(gsl_vector_int * fathers,vector<vector<int> > *slvs,int f) {
        for (unsigned int i=0;i<slvs->at(f).size();i++)
            if (gsl_vector_int_get(fathers,slvs->at(f).at(i))==-1) {
            gsl_vector_int_set(fathers,slvs->at(f).at(i),f);
            makeFathers(fathers,slvs,slvs->at(f).at(i));
        }

    }

    vector<vector<int> > * Burst::makeClusters(vector<int> *v,gsl_vector_int * fathers,int f,bool top) {
        vector<int> all;//cluster containing all sequences
        vector<vector<int> > * res=new vector<vector<int> >;
        for (unsigned int i=0;i<fathers->size;i++)
            if (gsl_vector_int_get(fathers,i)==f) {
            //make clusters starting from i
            vector<vector<int> > * t=makeClusters(v,fathers,i,true);
            //add these clusters
            if (top==true) {
                for (unsigned int j=0;j<t->size();j++)
                    res->push_back(t->at(j));}
                    else {
                        res->push_back(t->at(0));
                        for (unsigned int j=1;j<t->size();j++)
                            if (t->at(j).size()==1) res->push_back(t->at(j));
                    }
                    //and add all sts descending from i to the list of all sts
                    for (unsigned int j=0;j<t->back().size();j++)
                        all.push_back(t->back().at(j));
                }
        //add f to all
        all.push_back(v->at(f));
        //add all to res
        res->push_back(all);
        return res;
    }

}
