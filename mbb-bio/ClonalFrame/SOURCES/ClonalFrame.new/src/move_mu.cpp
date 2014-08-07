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
#include "move_mu.h"

namespace wb {

    Move_mu::Move_mu(gsl_rng * rng,Param * p):Move(rng) {}

    void Move_mu::move(Param *p) {
        double oldmu=p->mu;
        double oldll=p->tree->ll;
        if (p->uniprior==false) {
            p->mu*=gsl_sf_exp(gsl_sf_log(p->thetabase)*((gsl_rng_uniform(rng)-0.5)/10.0));
            if (p->mu<1.0e-7 || p->mu>=10.0) {p->mu=oldmu;return;}
        } else {
            p->mu+=(gsl_rng_uniform(rng)-0.5)/10000.0;
            if (p->mu<=0.0 || p->mu>=1.0) {p->mu=oldmu;return;}
        }
        p->tree->llhood(p);
        double ll=p->tree->ll;
        double r2=gsl_rng_uniform(rng);
        if (p->verbose) printf("Mu move proposed: %f->%f %f->%f\n",oldmu,p->mu,oldll,ll);
        if (gsl_sf_log(r2)<ll-oldll) return;
        p->mu=oldmu;
        p->tree->reverseall();
    }

    Move_mu::~Move_mu() {}


}
