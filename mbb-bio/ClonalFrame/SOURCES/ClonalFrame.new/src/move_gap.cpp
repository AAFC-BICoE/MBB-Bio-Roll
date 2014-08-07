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
#include "move_gap.h"

namespace wb {

    Move_gap::Move_gap(gsl_rng * rng,Param * p) : Move(rng) {}

    void Move_gap::move(Param *p) {
        double pmut,r;
        for (int i=0;i<p->a->getN();i++) {
            Tree * t=p->where[i];
            for (int j=0;j<p->a->getL();j++) {
                if (p->a->getData(i,j)!='N') continue;
                pmut=p->mu*(t->father->age-t->age);
                if (gsl_vector_char_get(t->recMap,j)==1) pmut=p->nu;
                r=gsl_rng_uniform(rng);
                if (r<pmut/3.0)   {gsl_vector_char_set(t->ancSeq,j,(gsl_vector_char_get(t->father->ancSeq,j)-'0'+1)%4+'0');continue;}
                if (r<2.0*pmut/3.0) {gsl_vector_char_set(t->ancSeq,j,(gsl_vector_char_get(t->father->ancSeq,j)-'0'+2)%4+'0');continue;}
                if (r<pmut)     {gsl_vector_char_set(t->ancSeq,j,(gsl_vector_char_get(t->father->ancSeq,j)-'0'+3)%4+'0');continue;}
                gsl_vector_char_set(t->ancSeq,j,gsl_vector_char_get(t->father->ancSeq,j));
            }
        }
    }


    Move_gap::~Move_gap() {}


}
