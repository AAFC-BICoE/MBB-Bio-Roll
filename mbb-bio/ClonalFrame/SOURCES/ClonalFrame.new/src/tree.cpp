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
#include "tree.h"
#include "param.h"

namespace wb {

    Tree::Tree() {
        id=0;
        ll=0.0;
        llb=0.0;
        oldll=0.0;
        oldllb=0.0;
        age=0.0;
        nodes=NULL;
        left=NULL;
        right=NULL;
        father=NULL;
        ancSeq=NULL;
        recMap=NULL;
    }

    Tree::~Tree() {
        if (ancSeq!=NULL) gsl_vector_char_free(ancSeq);
        if (recMap!=NULL) gsl_vector_char_free(recMap);
        //if (left!=NULL) delete(left);
        //if (right!=NULL) delete(right);
        free(nodes);
        //free(where);
    }

    void Tree::updateNodes() {
        if (left==NULL)
            n=1;
        else {
            left->updateNodes();
            right->updateNodes();
            n=left->n+right->n;
        }
        nodes[0]=this;
        if (left!=NULL) {
            for (int i=0;i<left->n-1;i++)
                nodes[i+1]=left->nodes[i];
            for (int i=0;i<right->n-1;i++)
                nodes[i+1+left->n-1]=right->nodes[i];
        }

    }

    Tree * Tree::move(Tree * x,Tree * y,double newAge,gsl_vector_char * ancSeq,gsl_vector_char * recMap,Param * p) {
        if (x->father==y->father) {Tree * root=x;while (root->father!=NULL) root=root->father;return root;}
        Tree * root=p->tree;
        //Tree ** where=(Tree**)calloc(p->a->getN(),sizeof(Tree*));
        //for (int i=0;i<p->a->getN();i++) where[i]=root->where[i];
        Tree * z=y->father;
        Tree * xfather=x->father;
        Tree * xgfather=xfather->father;
        Tree * xbro;
        if (xfather->left==x)
            xbro=xfather->right;
        else
            xbro=xfather->left;
        if (xgfather!=NULL) {
            if (xgfather->left==xfather)
                xgfather->left=xbro;
            else
                xgfather->right=xbro;
            xbro->father=xgfather;
        } else
            xbro->father=NULL;
        Tree * newNode=new Tree();
        //newNode->where=(Tree **)calloc(p->a->getN(),sizeof(Tree *));
        newNode->nodes=(Tree **)calloc(p->a->getN(),sizeof(Tree *));
        newNode->recMap=recMap;
        newNode->ancSeq=ancSeq;
        newNode->age=newAge;
        newNode->father=z;
        newNode->left=x;
        newNode->right=y;
        newNode->n=0;

        if (z!=NULL)
            if (z->left==y)
                z->left=newNode;
        else
            z->right=newNode;
        x->father=newNode;
        y->father=newNode;
        //if (xgfather!=NULL) {if (xgfather->left==xfather) xgfather->left=xbro; else xgfather->right=xbro;
        //xbro->father=xgfather;} else xbro->father=NULL;
        delete(xfather);

        root=x;
        while (root->father!=NULL) {
            root=root->father;
        }
        //free(root->where);
        //root->where=where;
        root->updateNodes();
        return root;
    }

    double Tree::llhood(Param * p) {
        if (p->verbose && this==p->tree) {printf("LLhood calculation with params mu=%e nu=%e rho=%e delta=%e\n",p->mu,p->nu,p->rho,p->delta);
            for (int i=0;i<p->a->getL();i++) gsl_vector_char_set(p->cf,i,0);
            p->rec=0;
            p->mut=0;
            p->mutrec=0;}
        double ret=0.0;
        ret=llhoodb(p);
        //printf("lldb for %d=%f\n",this->id,ret);
        //if (father!=NULL) {
        //for (int i=0;i<p->a->getL();i++) printf("%c",100+gsl_vector_char_get(recMap,i));printf("\n");
        //for (int i=0;i<p->a->getL();i++) printf("%c",gsl_vector_char_get(father->ancSeq,i));printf("\n");
        //}
        if (left!=NULL) {
            ret+=left->llhood(p);
            ret+=right->llhood(p);
        }
        oldll=ll;
        ll=ret;
        //if (p->verbose && this==p->tree) {
        //int sum=0;
        //for (int i=0;i<p->a->getL();i++) sum+=gsl_vector_char_get(p->cf,i);
        //printf("mut=%d,rec=%d,mutrec=%d,cf=%d\n",p->mut,p->rec,p->mutrec,p->a->getL()-sum);}
        return ret;
    }

    void Tree::updatellgivenllb() {
        ll=llb;
        if (left!=NULL) {
            left->updatellgivenllb();
            right->updatellgivenllb();
            ll+=left->ll;
            ll+=right->ll;
        }
    }

    /*double Tree::llhoodT(Param * p) {
//if (n!=p->a->getN()) printf("ERROR %d %d\n",n,p->a->getN());
    double ret=0.0;
    gsl_vector * ages=gsl_vector_calloc(n);
    for (int i=0;i<n-1;i++)
        gsl_vector_set(ages,i,nodes[i]->age);
    gsl_vector_set(ages,n-1,0.0);
    gsl_sort_vector(ages);//sorts in ascending numerical order
    for (int i=1;i<n;i++)
        ret-=((n-i)*(n-i+1.0)/2.0)*(gsl_vector_get(ages,i)-gsl_vector_get(ages,i-1));
    gsl_vector_free(ages);
    return ret;
}*/

    double Tree::llhoodT(Param * p) {
        double ret=0.0;
        double beta=p->expgrowth;
        gsl_vector * ages=gsl_vector_calloc(n);
        for (int i=0;i<n-1;i++)
            gsl_vector_set(ages,i,nodes[i]->age);
        gsl_vector_set(ages,n-1,0.0);
        gsl_sort_vector(ages);//sorts in ascending numerical order
        double prev=0.0;
        double cur;
        for (int i=1;i<n;i++) {
            cur=(gsl_sf_exp(beta*gsl_vector_get(ages,i))-1)/beta;
            ret+=beta*gsl_vector_get(ages,i)-((n-i)*(n-i+1.0)/2.0)*(cur-prev);
            prev=cur;}

        gsl_vector_free(ages);
        return ret;
    }

    double Tree::llhoodb(Param * p) {
        //if (father!=NULL) printf("%f %f %f %f %f %f\n",p->mu,p->rho,p->nu,p->delta,father->age,age);
        //else printf("%f %f %f %f ROOT %f\n",p->mu,p->rho,p->nu,p->delta,age);
        double ret=0.0;
        if (father!=NULL) {
            double diffage=father->age-age;
            if (diffage==0) diffage=10e-10;
            double mu=p->mu*diffage;
            double vals[10];
            vals[0]=gsl_sf_log(1.0-mu);
            vals[1]=gsl_sf_log(mu/3.0);
            vals[2]=gsl_sf_log(1.0-p->nu);
            vals[3]=gsl_sf_log(p->nu/3.0);
            vals[4]=gsl_sf_log(1.0-p->rho*diffage);
            if (p->rho>0.0) vals[5]=gsl_sf_log(p->rho*diffage);
            vals[6]=gsl_sf_log(p->delta);
            vals[7]=gsl_sf_log(1.0-p->delta);
            vals[8]=gsl_sf_log(p->delta/(p->delta+p->rho*diffage));
            if (p->rho>0.0) vals[9]=gsl_sf_log(p->rho*diffage/(p->delta+p->rho*diffage));
            for (int i=0;i<p->a->getL();i++) {
                if (gsl_vector_char_get(recMap,i)==UNLINKED)
                {gsl_vector_char_set(p->cf,i,1);continue;}
                if (gsl_vector_char_get(ancSeq,i)==gsl_vector_char_get(father->ancSeq,i)) {
                    if (gsl_vector_char_get(recMap,i)==0) {ret+=vals[0];}
                    else {gsl_vector_char_set(p->cf,i,1);ret+=vals[2];}
                } else
                    if (gsl_vector_char_get(recMap,i)==0) {ret+=vals[1];p->mut++;}
                else {gsl_vector_char_set(p->cf,i,1);ret+=vals[3];p->mutrec++;}

                if (i>0 && gsl_vector_char_get(recMap,i-1)!=UNLINKED) {
                    if (gsl_vector_char_get(recMap,i-1)==0) {
                        if (gsl_vector_char_get(recMap,i)==0)
                        {ret+=vals[4];}
                        else
                        {ret+=vals[5];p->rec++;}
                    } else
                        if (gsl_vector_char_get(recMap,i)==0)
                        {ret+=vals[6];}
                    else
                    {ret+=vals[7];}
                } else if (gsl_vector_char_get(recMap,i)==0) {ret+=vals[8];} else {ret+=vals[9];p->rec++;}
            }
        }
        oldllb=llb;
        llb=ret;
        return ret;
    }

    void Tree::count(Param * p,double * mut,double * rec,double * mutrec,gsl_vector_char * cf)
    {
        if (father==NULL) return;
        for (int i=0;i<p->a->getL();i++) {

            if (gsl_vector_char_get(recMap,i)==UNLINKED) {gsl_vector_char_set(cf,i,1);continue;}
            if (gsl_vector_char_get(ancSeq,i)==gsl_vector_char_get(father->ancSeq,i)) {
                if (gsl_vector_char_get(recMap,i)!=0) gsl_vector_char_set(cf,i,1);
            } else
                if (gsl_vector_char_get(recMap,i)==0) (*mut)++;
            else {gsl_vector_char_set(cf,i,1);(*mutrec)++;}

            if (i>0 && gsl_vector_char_get(recMap,i-1)!=UNLINKED) 
            {if (gsl_vector_char_get(recMap,i-1)==0 && gsl_vector_char_get(recMap,i)!=0) (*rec)++;}
            else if (gsl_vector_char_get(recMap,i)!=0) (*rec)++;

        }

        father->count(p,mut,rec,mutrec,cf);
    }

    void Tree::countInterIntra(Param * p,int *mutin,int *mutout,int *recin,int *recout)
    {
        bool in;//true if a substitution is found somewhere else in the dataset
        if (father!=NULL) {
            //Firstly determine the children of the current node
            gsl_vector_int *children=gsl_vector_int_calloc(p->a->getN());
            Tree * k;
            for (int i=0;i<p->a->getN();i++) {
                k=p->where[i];
                while (k!=NULL && k!=this) k=k->father;
                if (k==this) gsl_vector_int_set(children,i,1);
            }
            //Secondly determine if each substitution is in or out
            for (int i=0;i<p->a->getL();i++) {
                if (gsl_vector_char_get(recMap,i)==UNLINKED) continue;
                if (gsl_vector_char_get(ancSeq,i)==gsl_vector_char_get(father->ancSeq,i)) continue;
                in=false;
                for (int j=0;j<p->a->getN();j++) {
                    if (gsl_vector_int_get(children,j)==0 && gsl_vector_char_get(ancSeq,i)==gsl_vector_char_get(p->where[j]->ancSeq,i)) {in=true;break;};
                }
                //Thirdly record the type (in/out,mut/mutrec) of each substitution
                if (gsl_vector_char_get(recMap,i)==0 && in==false) (*mutout)++;
                if (gsl_vector_char_get(recMap,i)!=0 && in==false) (*recout)++;
                if (gsl_vector_char_get(recMap,i)==0 && in==true) (*mutin)++;
                if (gsl_vector_char_get(recMap,i)!=0 && in==true) (*recin)++;
            }
            gsl_vector_int_free(children);
        }
        if (left!=NULL) {
            left ->countInterIntra(p,mutin,mutout,recin,recout);
            right->countInterIntra(p,mutin,mutout,recin,recout);
        }
    }

    void Tree::reverseall()
    {
        ll=oldll;
        llb=oldllb;
        if (left!=NULL) {
            left->reverseall();
            right->reverseall();
        }
    }

    /**
 * 
 * @param where 
 * @param nodes 
 * @param min 
 * @return 
 */
    char * Tree::newick(Tree ** where,Tree ** nodes,int * min) {
        char * buf;
        //double fage;
        //if (father==NULL) fage=age;else fage=father->age;
        if (left!=NULL) {
            //Internal node
            int a=0,b=0;
            char * l=left->newick(where,nodes,&a);
            char * r=right->newick(where,nodes,&b);
            buf=(char *)calloc(strlen(l)+strlen(r)+50,sizeof(char));
            int i=0;
            while (this!=nodes[i])
                i++;
            if (a<b)
                sprintf(buf,"(%s,%s):%f",l,r,age);
            else
                sprintf(buf,"(%s,%s):%f",r,l,age);
            free(l);
            free(r);
            if (min!=NULL)
                *min=GSL_MIN(a,b);
        } else {
            buf=(char *)calloc(1000,sizeof(char));
            //Leaf
            int i=0;
            while (this!=where[i])
                i++;
            sprintf(buf,"%d:%f",i+1,age);
            if (min!=NULL)
                *min=i;
        }
        return buf;
    }

    void Tree::ungap(gsl_vector_char * seq,Param * p) {
        int k;
        gsl_vector_int * freqs=gsl_vector_int_calloc(4);
        for (int i=0;i<p->a->getL();i++) {
            if (gsl_vector_char_get(seq,i)!='N') continue;
            for (k=0;k<4;k++)
                gsl_vector_int_set(freqs,k,0);
            for (k=0;k<p->a->getN();k++)
                if (p->a->getData(k,i)>='0' && p->a->getData(k,i)<='3')
                    (*gsl_vector_int_ptr(freqs,p->a->getData(k,i)-'0'))++;
            gsl_vector_char_set(seq,i,gsl_vector_int_max_index(freqs)+'0');
        }
        gsl_vector_int_free(freqs);
    }

    void Tree::fixtimes(double tottime)
    {
        age=tottime-age;
        if (left!=NULL) {left->fixtimes(tottime);right->fixtimes(tottime);}
    }

    double Tree::depth()
    {
        if (left==NULL) return 0.0;
        return 1.0+GSL_MAX(left->depth(),right->depth());
    }

}

