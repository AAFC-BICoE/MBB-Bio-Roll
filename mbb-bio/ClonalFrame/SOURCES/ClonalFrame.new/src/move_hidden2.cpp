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
#include "move_hidden2.h"

namespace wb {

    Move_hidden2::Move_hidden2(gsl_rng * rng,Param * p) : Move(rng)
    {
        mh=new Move_hidden(rng,p);
    }

    void Move_hidden2::move(Param * p)
    {
        printf("Move hidden 2\n");
        p->tree->llhood(p);
        Tree ** nodes=p->tree->nodes;
        for (int i=p->a->getN()-2;i>=0;i--){
            Tree * x=nodes[i]->left;
            Tree * y=nodes[i]->right;
            double l1=nodes[i]->llb+x->llb+y->llb;
            gsl_vector_char * ancSeq=gsl_vector_char_calloc(p->a->getL());
            gsl_vector_char * recMap=gsl_vector_char_calloc(p->a->getL());
            gsl_vector_char * recMapx=gsl_vector_char_calloc(p->a->getL());
            gsl_vector_char * recMapy=gsl_vector_char_calloc(p->a->getL());
            gsl_vector_char_memcpy(ancSeq,nodes[i]->ancSeq);
            gsl_vector_char_memcpy(recMap,nodes[i]->recMap);
            gsl_vector_char_memcpy(recMapx,x->recMap);
            gsl_vector_char_memcpy(recMapy,y->recMap);
            mh->calculMode=true;
            mh->move1(p,nodes[i]);
            double q1=mh->pprop;
            mh->calculMode=false;
            mh->move1(p,nodes[i]);
            double q2=mh->pprop;
            nodes[i]->llhoodb(p);
            x->llhoodb(p);
            y->llhoodb(p);
            double l2=nodes[i]->llb+x->llb+y->llb;
            double alpha=l2-l1+q1-q2;
            double rnd=gsl_rng_uniform(p->rng);
            printf("lrnd=%f Alpha=%e=%e-%e+%e-%e\n",gsl_sf_log(rnd),alpha,l2,l1,q1,q2);
            //if (alpha>1.0 || alpha<-1.0) exit(0);
            if (false && gsl_sf_log(rnd)>alpha) {
                //Rollback
                printf("Move hidden 2 rejected\n");
                gsl_vector_char_free(x->recMap);
                x->recMap=recMapx;
                gsl_vector_char_free(y->recMap);
                y->recMap=recMapy;
                gsl_vector_char_free(nodes[i]->ancSeq);
                nodes[i]->ancSeq=ancSeq;
                gsl_vector_char_free(nodes[i]->recMap);
                nodes[i]->recMap=recMap;
                nodes[i]->llb=nodes[i]->oldllb;
                x->llb=x->oldllb;
                y->llb=y->oldllb;
            } else {
                printf("Move hidden 2 accepted\n");
                gsl_vector_char_free(ancSeq);
                gsl_vector_char_free(recMap);
                gsl_vector_char_free(recMapx);
                gsl_vector_char_free(recMapy);
            }
        }
        p->tree->llhood(p);//Recalculate the likelihoods
    }

    Move_hidden2::~Move_hidden2()
    {
        delete mh;
    }


}
