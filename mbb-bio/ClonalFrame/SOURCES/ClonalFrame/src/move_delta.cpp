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
#include "move_delta.h"

namespace wb {

    Move_delta::Move_delta(gsl_rng * rng,Param * p):Move(rng) {
    }

    void Move_delta::move(Param *p) {
        double olddelta=p->delta;
        double oldll=p->tree->ll;
        if (p->uniprior==false) {
            p->delta*=gsl_sf_exp(gsl_sf_log(p->deltabase)*((gsl_rng_uniform(rng)-0.5)/10.0));
            if (p->delta<1.0e-7 || p->delta>0.1) {p->delta=olddelta;return;}
        } else {
            p->delta+=(gsl_rng_uniform(rng)-0.5)/10000.0;
            if (p->delta<=0.0 || p->delta>=1.0) {p->delta=olddelta;return;}
        }
        p->tree->llhood(p);
        double ll=p->tree->ll;
        double r2=gsl_rng_uniform(rng);
        if (p->verbose) printf("Delta move proposed: %f->%f %f->%f\n",olddelta,p->delta,oldll,ll);
        if (gsl_sf_log(r2)<ll-oldll) return;
        p->delta=olddelta;
        p->tree->reverseall();
    }

    Move_delta::~Move_delta() {}


}
