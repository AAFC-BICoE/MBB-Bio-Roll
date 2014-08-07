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
#include "move_rho.h"

namespace wb {

    Move_rho::Move_rho(gsl_rng * rng,Param * p):Move(rng)
    {
    }

    void Move_rho::move(Param *p) {
        double oldrho=p->rho;
        double oldll=p->tree->ll;
        if (p->uniprior==false) {
            p->rho*=gsl_sf_exp(gsl_sf_log(p->Rbase)*((gsl_rng_uniform(rng)-0.5)/10.0));
            if (p->rho<1.0e-7 || p->rho>0.1) {p->rho=oldrho;return;}
        } else {
            p->rho+=(gsl_rng_uniform(rng)-0.5)/10000.0;
            if (p->rho<=0.0 || p->rho>=1.0) {p->rho=oldrho;return;}
        }


        p->tree->llhood(p);
        double ll=p->tree->ll;
        double r2=gsl_rng_uniform(rng);
        if (p->verbose) printf("Rho move proposed: %f->%f %f->%f\n",oldrho,p->rho,oldll,ll);
        if (gsl_sf_log(r2)<ll-oldll) return;
        p->rho=oldrho;
        p->tree->reverseall();
    }

    Move_rho::~Move_rho() {}


}
