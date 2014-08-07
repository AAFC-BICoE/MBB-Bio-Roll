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
#include "tree_coal.h"

namespace wb {

    Tree_coal::Tree_coal(Param * p,Tree *** where)
        : Tree()
    {
        //Init
        id=0;
        n=p->a->getN();
        (*where)=(Tree **)calloc(n,sizeof(Tree *));
        father=NULL;
        nodes=(Tree **)calloc(n,sizeof(Tree *));
        //First simulate the coalescent using forward in time algorithm
        int k=1;
        Tree ** lines=(Tree **)calloc(n,sizeof(Tree*));
        lines[0]=this;
        double tottime=0.0;
        while (k<n) {
            int tosplit=gsl_rng_uniform_int(p->rng,k);
            if (k>1) tottime+=gsl_ran_exponential(p->rng,2.0/((k-1.0)*k));
            lines[tosplit]->age=tottime;
            Tree * l=new Tree();
            Tree * r=new Tree();
            l->nodes=(Tree **)calloc(n,sizeof(Tree *));
            r->nodes=(Tree **)calloc(n,sizeof(Tree *));
            l->father=lines[tosplit];
            r->father=lines[tosplit];
            lines[tosplit]->left=l;
            lines[tosplit]->right=r;
            lines[tosplit]=l;
            lines[k]=r;
            k++;
        }
        tottime+=gsl_ran_exponential(p->rng,2.0/((k-1.0)*k));
        for (int i=0;i<n;i++) lines[i]->age=tottime;
        fixtimes(tottime);

        //Then assign ids to leaves and make "where"
        int * assigned=(int *)calloc(n,sizeof(int));
        for (int i=0;i<n;i++) {
            rep:int w=gsl_rng_uniform_int(p->rng,n);
                bool ok=true;
                for (int j=0;j<i;j++) if (assigned[j]==w) ok=false;
                if (ok==false) goto rep;
                (*where)[i]=lines[w];
                lines[w]->id=i;
                assigned[i]=w;
                lines[w]->ancSeq=gsl_vector_char_calloc(p->a->getL());
                lines[w]->recMap=gsl_vector_char_calloc(p->a->getL());
                for (int j=0;j<p->a->getL();j++)
                    gsl_vector_char_set(lines[w]->ancSeq,j,p->a->getData(i,j));
                ungap(lines[w]->ancSeq,p);
            }

        //Make "nodes" and "n" and ancSeq of internal nodes
        updateNodes();
        for (int j=n-2;j>=0;j--) {
            nodes[j]->ancSeq=gsl_vector_char_calloc(p->a->getL());
            nodes[j]->recMap=gsl_vector_char_calloc(p->a->getL());
            for (int i=0;i<p->a->getL();i++) if (gsl_rng_uniform(p->rng)<
                                                 (nodes[j]->age-nodes[j]->right->age)/(2.0*nodes[j]->age-nodes[j]->right->age-nodes[j]->left->age))
                gsl_vector_char_set(nodes[j]->ancSeq,i,gsl_vector_char_get(nodes[j]->left->ancSeq,i));
            else gsl_vector_char_set(nodes[j]->ancSeq,i,gsl_vector_char_get(nodes[j]->right->ancSeq,i));
        }

        //Clear the memory
        free(assigned);
        free(lines);
    }

    Tree_coal::~Tree_coal()
    {
    }


}
