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
#include "consensus.h"

namespace wb {

    Consensus::Consensus(Param *p,int t) {
        this->n=p->a->getN();
        this->p=p;
        this->t=t;
        hashTable=(HashCell **)calloc(n*t,sizeof(HashCell *));
        a=gsl_vector_int_calloc(n);
        for (int i=0;i<n;i++)
            gsl_vector_int_set(a,i,gsl_rng_uniform_int(p->rng,n));
        nbtokeep=0;
        tokeep=(HashCell**)calloc(2*n-1,sizeof(HashCell*));
    }

    void Consensus::addTree(Tree *t) {
        for (int i=0;i<n-1;i++)
            addNode(t->nodes[i]);
        for (int i=0;i<n;i++)
            addNode(p->where[i]);
    }

    void Consensus::addNode(Tree *t) {
        bool * id=calid(t);
        int h=hash(id);
        HashCell * hc=hashTable[h];
        while (hc!=NULL) {
            if (eq(hc->id,id))
                break;
            else
                hc=hc->next;
        }
        if (hc==NULL) {
            hc=new HashCell(id,p);
            hc->next=hashTable[h];
            hashTable[h]=hc;
        } else
            free(id);
        hc->addNode(t);
    }

    bool Consensus::eq(bool*a,bool*b) {
        for (int i=0;i<n;i++)
            if (a[i]!=b[i])
                return false;
        return true;
    }

    bool Consensus::incl(bool*a,bool*b) {
        for (int i=0;i<n;i++)
            if (a[i]==true && b[i]==false)
                return false;
        return true;
    }

    int Consensus::sum(bool*a) {
        int s=0;
        for (int i=0;i<n;i++)
            if (a[i]==true)
                s++;
        return s;
    }

    int Consensus::first(bool*a) {
        for (int i=0;i<n;i++) if (a[i]==true) return i;
        return -1;
    }

    bool * Consensus::calid(Tree * t) {
        bool * res=(bool *)calloc(n,sizeof(bool));
        ad(res,t);
        return res;
    }

    void Consensus::ad(bool * res,Tree * t) {
        if (t->left==NULL)
            res[t->id]=true;
        else {
            ad(res,t->left);
            ad(res,t->right);
        }
    }

    void Consensus::minus(bool*a,bool*b) {
        for (int i=0;i<n;i++)
            if (b[i]==true)
                a[i]=false;
    }

    bool* Consensus::copy(bool *a) {
        bool *res=(bool*)calloc(n,sizeof(bool));
        for (int i=0;i<n;i++) res[i]=a[i];
        return res;
    }

    int Consensus::hash(bool * id) {
        int res=0;
        for (int i=0;i<n;i++)
            if (id[i]==true)
                res=(res+gsl_vector_int_get(a,i))%(n*t);
        return res;
    }

    char * Consensus::retConsensus(double cutoff) {
        //First decide which partitions to keep
        HashCell * ptr;
        nbtokeep=0;
        //Add partitions of size 1
        for (int i=0;i<n;i++) {
            ptr=hashTable[gsl_vector_int_get(a,i)%(n*t)];
            while (ptr!=NULL) {
                if (first(ptr->id)==i && sum(ptr->id)==1 && ptr->nb>t*cutoff)
                    tokeep[nbtokeep++]=ptr;
                ptr=ptr->next;
            }
        }
        //Add other partitions
        for (int i=0;i<n*t;i++) {
            ptr=hashTable[i];
            while (ptr!=NULL) {
                if (sum(ptr->id)>1 && ptr->nb>t*cutoff)
                    tokeep[nbtokeep++]=ptr;
                ptr=ptr->next;
            }
        }

        //Then build a tree based on these partitions
        bool all[n];
        for (int i=0;i<n;i++)
            all[i]=true;
        int i=0;
        while (!eq(tokeep[i]->id,all))
            i++;
        char * res=buildsubtree(i,tokeep,nbtokeep);
        sprintf(res+strlen(res),":0.000000");
        return res;
    }

    char * Consensus::buildsubtree(int w,HashCell ** tokeep,int nbtokeep) {
        bool * els=copy(tokeep[w]->id);
        int card=sum(els);
        double age=tokeep[w]->age/tokeep[w]->nb;
        char * res=(char *)calloc(100000,sizeof(char));
        int pos=0;
        pos+=sprintf(res+pos,"(");
        for (int i=card-1;i>0;i--) {
            for (int j=0;j<nbtokeep;j++)
                if (sum(tokeep[j]->id)==i && incl(tokeep[j]->id,els)) {
                char * r;
                if (i==1) {
                    pos+=sprintf(res+pos,"%d:%f,",first(tokeep[j]->id)+1,age);
                } else {
                    r=buildsubtree(j,tokeep,nbtokeep);
                    pos+=sprintf(res+pos,"%s:%f,",r,age-tokeep[j]->age/tokeep[j]->nb);
                    free(r);}
                minus(els,tokeep[j]->id);
            }
        }
        sprintf(res+pos-1,")%d",w+1);
        free(els);
        return res;
    }

    Consensus::~Consensus() {
        gsl_vector_int_free(a);
        for (int i=0;i<n*t;i++)
            delete(hashTable[i]);
        free(hashTable);
        free(tokeep);
    }

}
