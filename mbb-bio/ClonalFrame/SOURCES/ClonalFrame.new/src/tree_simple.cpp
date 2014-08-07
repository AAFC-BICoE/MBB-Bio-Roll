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
#include "tree_simple.h"

namespace wb {

    Tree_simple::Tree_simple(Param * p,Tree *** where)
        : Tree()
    {
        id=0;
        n=p->a->getN();
        (*where)=(Tree **)calloc(p->a->getN(),sizeof(Tree *));
        init(p,n);
        father=NULL;
        updateNodes();
        Tree * t=this;
        for (int i=n-1;i>0;i--) {
            (*where)[i]=t->left;
            t->left->id=i;
            t=t->right;
        };
        (*where)[0]=t;
        t->id=0;
    }

    Tree_simple::Tree_simple(Param * p,int n,Tree * father) {
        id=0;
        this->n=n;
        init(p,n);
        this->father=father;
    }

    void Tree_simple::init(Param * p,int n) {
        ll=0.0;
        llb=0.0;
        oldll=0.0;
        oldllb=0.0;
        //where=(Tree **)calloc(p->a->getN(),sizeof(Tree *));
        ancSeq=gsl_vector_char_calloc(p->a->getL());
        recMap=gsl_vector_char_calloc(p->a->getL());
        if (n>1) {
            left=new Tree_simple(p,1,this);
            for (int i=0;i<p->a->getL();i++)
                gsl_vector_char_set(left->ancSeq,i,p->a->getData(n-1,i));
            ungap(left->ancSeq,p);
            //where[n-1]=left;
            right=new Tree_simple(p,n-1,this);
            if (n==2) {
                for (int i=0;i<p->a->getL();i++)
                    gsl_vector_char_set(right->ancSeq,i,p->a->getData(0,i));//where[0]=right;
                ungap(right->ancSeq,p);
            }

            for (int i=0;i<p->a->getL();i++) if (gsl_rng_uniform(p->rng)<1.0/n)
                gsl_vector_char_set(ancSeq,i,gsl_vector_char_get(left->ancSeq,i));
            else gsl_vector_char_set(ancSeq,i,gsl_vector_char_get(right->ancSeq,i));
            //if (n>2) for (int i=0;i<n-1;i++) where[i]=right->where[i];
        } else {
            left=NULL;
            right=NULL;
        }
        nodes=(Tree **)calloc(p->a->getN(),sizeof(Tree *));
        //if (n>1) nodes[0]=this;
        //if (n>2) for (int i=0;i<right->n-1;i++) nodes[i+1]=right->nodes[i];
        if (n==1)
            age=0.0;
        else
            age=GSL_MAX(left->age,right->age)+1.0;
    }

    Tree_simple::~Tree_simple()
    {
    }


}
