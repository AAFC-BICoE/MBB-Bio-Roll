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
#include "move_nu.h"

namespace wb {

    Move_nu::Move_nu(gsl_rng * rng,Param * p):Move(rng) {}

    /*void Move_nu::move(Param *p) {
    double oldnu=p->nu;
    double oldll=p->tree->ll;
    if (p->uniprior==false) {
    p->nu*=gsl_sf_exp(((gsl_rng_uniform(rng)-0.5)/10.0));
    if (p->nu<1.0e-7 || p->nu>0.1) {p->nu=oldnu;return;}
    } else {
    p->nu+=(gsl_rng_uniform(rng)-0.5)/10000.0;
    if (p->nu<=0.0 || p->nu>=1.0) {p->nu=oldnu;return;}
    }
    p->tree->llhood(p);
    double ll=p->tree->ll;
    double r2=gsl_rng_uniform(rng);
    printf("Nu move proposed: %f->%f %f->%f\n",oldnu,p->nu,oldll,ll);
    if (gsl_sf_log(r2)<ll-oldll) return;
    p->nu=oldnu;
    p->tree->reverseall();

}*/

    void Move_nu::move(Param *p) {
        double a=p->nubeta1;
        double b=p->nubeta2;
        Tree * t;
        for (int i=0;i<p->a->getN()*2-2;i++)
            for (int j=0;j<p->a->getL();j++) {
            if (i<p->a->getN())
                t=p->where[i];
            else
                t=p->tree->nodes[i+1-p->a->getN()];
            if (gsl_vector_char_get(t->recMap,j)==1)
                if (gsl_vector_char_get(t->ancSeq,j)!=gsl_vector_char_get(t->father->ancSeq,j))
                    a++;
            else
                b++;
        }

        p->nu=gsl_ran_beta(rng,a,b);
        if (p->verbose) printf("Updating nu:%f %f %f %f\n",p->tree->ll,p->nu,a,b);
    }

    Move_nu::~Move_nu() {}



}
