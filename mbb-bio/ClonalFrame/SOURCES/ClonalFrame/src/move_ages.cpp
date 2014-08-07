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
#include "move_ages.h"

namespace wb {

    Move_ages::Move_ages(gsl_rng* rng): Move(rng) {}


    Move_ages::~Move_ages() {}


    void Move_ages::move(Param* p) {
        double oldAge,r;
        Tree * a;
        for (int i=0;i<p->a->getN()-1;i++)//For each internal node
        {
            a=p->tree->nodes[i];
            oldAge=a->age;
            r=(gsl_rng_uniform(rng)-0.5)*0.1;
            if (oldAge+r>0.0 && (a->father==NULL || a->father->age>oldAge+r) && a->left->age<oldAge+r && a->right->age<oldAge+r) {
                double oldllT=p->tree->llhoodT(p);
                a->age=oldAge+r;
                double llT=p->tree->llhoodT(p);
                //p->tree->llhood(p);
                a->llhoodb(p);
                a->left->llhoodb(p);
                a->right->llhoodb(p);
                r=gsl_rng_uniform(rng);
                double ll1,ll2;
                ll1=a->oldllb+a->left->oldllb+a->right->oldllb+oldllT;
                ll2=a->llb+a->left->llb+a->right->llb+llT;
                if (gsl_sf_log(r)<ll2-ll1) {
                    p->tree->updatellgivenllb();
                    //printf("Age change accepted %f %f Llhood=%f\n",ll1,ll2,p->tree->ll);
                } else {
                    //printf("Age change rejected %f %f Llhood=%f\n",ll1,ll2,p->tree->ll);
                    a->age=oldAge;
                    a->llb=a->oldllb;
                    a->left->llb=a->left->oldllb;
                    a->right->llb=a->right->oldllb;
                }
            } else  ;//printf("Age change rejected because out of range\n");
        }
        /*
//This checks that the move_ages move keeps the likelihood alright
double ll1=p->tree->llhoodsum(p);
double ll2=p->tree->llhood(p);
if (ll1!=ll2) {printf("error0 %f %f\n",ll1,ll2);exit(0);}
*/
    }


}
