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
#include "move_wb.h"
#include "timeval.h"

namespace wb {

    Move_wb::Move_wb(gsl_rng* rng,Param * p): Move(rng) {
        mh=new Move_hidden(rng,p);
        which=0;
        nbswaps=0;
        tlast=0;
    }

    Move_wb::~Move_wb() {
        delete(mh);
    }

    int Move_wb::propLocs(Tree ** ys,double * probys,Tree *x,Param * p) {
        int sizeys=0;
        for (int i=0;i<p->a->getN();i++)
            if (p->where[i]!=x && p->where[i]!=x->father && p->where[i]->father!=x->father && p->where[i]->father->age>x->age)
                ys[sizeys++]=p->where[i];
        if (x->father!=p->tree)
            ys[sizeys++]=p->tree;
        for (int i=1;i<p->a->getN()-1;i++)
            if (p->tree->nodes[i]!=x && p->tree->nodes[i]!=x->father && p->tree->nodes[i]->father!=x->father && p->tree->nodes[i]->father->age>x->age)
                ys[sizeys++]=p->tree->nodes[i];
        for (int i=0;i<sizeys;i++) probys[i]=1.0/(1.0+p->a->diff(ys[i]->ancSeq,x->ancSeq));//1.0;
        if (sizeys>0) Util::normalize(probys,sizeys);
        return sizeys;
    }

    void Move_wb::move(Param* p) {
        int repeats=0;
        struct timeval tv;
        gettimeofday(&tv,0);
        unsigned int tcur=tv.tv_sec*1000000+tv.tv_usec;//current time
        if (tlast==0) tlast=tcur;//will do only one iteration
        unsigned int tstop=tcur+(tcur-tlast);//time when we should stop
        while (nbswaps==0 || repeats<nbswaps)
        {
            repeats++;
            //First choose x,y and newAge
            beg:
            Tree * x;
            int r=(which++)%(p->a->getN()*2-2);//gsl_rng_uniform_int(p->rng,p->a->getN()*2-2);
            if (r<p->a->getN())
                x=p->where[r];
            else
                x=p->tree->nodes[r-p->a->getN()+1];
            Tree ** ys=(Tree **)calloc(p->a->getN()*2-1,sizeof(Tree *));
            double * probys=(double *)calloc(p->a->getN()*2-1,sizeof(double));
            int sizeys=propLocs(ys,probys,x,p);
            if (sizeys==0) {
                free(ys);
                free(probys);
                goto beg;
            }
            double r3=gsl_rng_uniform(p->rng);
            //r=gsl_rng_uniform_int(p->rng,sizeys);
            int r2=0;
            while (r3>probys[r2]) r3-=probys[r2++];
            Tree * y=ys[r2];
            double ppropy=probys[r2];
            if (p->verbose) printf("Proposing to move %d next to %d (proba=%f,nbys=%d)\n",x->id,y->id,probys[r2],sizeys);
            double max;
            if (y==p->tree)
                max=gsl_max(y->age,x->age)+y->age;
            else
                max=y->father->age;
            double newAge=gsl_rng_uniform(p->rng)*(max-gsl_max(y->age,x->age))+gsl_max(y->age,x->age);
            double range=(max-gsl_max(y->age,x->age));
            double range2=x->father->age-x->age;
            //Prepare for potential rollback
            double oldAge=x->father->age;
            Tree * xbro;
            if (x->father->left==x)
                xbro=x->father->right;
            else
                xbro=x->father->left;
            gsl_vector_char * ancSeq=gsl_vector_char_calloc(p->a->getL());
            gsl_vector_char * recMap=gsl_vector_char_calloc(p->a->getL());
            gsl_vector_char * recMapx=gsl_vector_char_calloc(p->a->getL());
            gsl_vector_char * recMapy=gsl_vector_char_calloc(p->a->getL());
            gsl_vector_char * recRoot=gsl_vector_char_calloc(p->a->getL());
            gsl_vector_char * recMapxbro=gsl_vector_char_calloc(p->a->getL());
            gsl_vector_char_memcpy(ancSeq,x->father->ancSeq);
            gsl_vector_char_memcpy(recMap,x->father->recMap);
            gsl_vector_char_memcpy(recMapx,x->recMap);
            gsl_vector_char_memcpy(recMapy,y->recMap);
            gsl_vector_char_memcpy(recRoot,p->tree->recMap);
            gsl_vector_char_memcpy(recMapxbro,xbro->recMap);
            double oldllhood=p->tree->ll;
            double oldyllb=y->llb;
            double oldxllb=x->llb;
            double oldxfatherllb=x->father->llb;
            double oldxbrollb=xbro->llb;
            double oldllhoodT=p->tree->llhoodT(p);
            mh->calculMode=true;
            mh->move1(p,x->father);
            double q=mh->pprop;
            mh->calculMode=false;
            //Change the tree
            p->tree=Tree::move(x,y,newAge,gsl_vector_char_calloc(p->a->getL()),gsl_vector_char_calloc(p->a->getL()),p);
            for (int i=0;i<p->a->getL();i++) if (gsl_vector_char_get(recMapx,i)==UNLINKED) gsl_vector_char_set(x->father->ancSeq,i,UNLINKED);
            for (int i=0;i<p->a->getL();i++) if (gsl_vector_char_get(recMapx,i)!=UNLINKED) gsl_vector_char_set(p->tree->recMap,i,0);
            mh->move1(p,x->father);
            //Compare likelihood of new tree with old tree
            int sizeys2=propLocs(ys,probys,x,p);
            r2=0;
            while (ys[r2]!=xbro) r2++;
            double ppropy2=probys[r2];
            x->llhoodb(p);
            y->llhoodb(p);
            x->father->llhoodb(p);
            xbro->llhoodb(p);
            p->tree->updatellgivenllb();

            //Check that the proposed configuration has right ll
            /*double lltmp=p->tree->ll;
if (fabs(lltmp-p->tree->llhood(p))>0.0001) {printf("error2 %f %f\n",lltmp,p->tree->llhood(p));exit(0);}*/

            double alpha=gsl_sf_log(range)-gsl_sf_log(range2)-gsl_sf_log(ppropy)+gsl_sf_log(ppropy2)+ p->tree->ll+p->tree->llhoodT(p)-oldllhood-oldllhoodT;
            alpha+=q-mh->pprop;
            double rnd=gsl_rng_uniform(p->rng);
            if (p->verbose) printf("%f %f -> %f %f\n",oldllhood,oldllhoodT,p->tree->ll,p->tree->llhoodT(p));
            if (gsl_sf_log(rnd)>alpha) {
                //Rollback the changes on the phylogeny
                if (p->verbose) printf("Move phylo rejected %f %f\n",oldllhood,p->tree->ll);
                p->tree=Tree::move(x,xbro,oldAge,ancSeq,recMap,p);
                gsl_vector_char_free(p->tree->recMap);
                p->tree->recMap=recRoot;
                gsl_vector_char_free(x->recMap);
                x->recMap=recMapx;
                gsl_vector_char_free(y->recMap);
                y->recMap=recMapy;
                //if (y->father!=NULL) //{gsl_vector_char_free(y->father->recMap);y->father->recMap=recMapyfather;}
                gsl_vector_char_free(xbro->recMap);
                xbro->recMap=recMapxbro;
                x->llb=oldxllb;
                y->llb=oldyllb;
                x->father->llb=oldxfatherllb;
                xbro->llb=oldxbrollb;
            } else {
                //Move accepted
                if (p->verbose) printf("Move phylo accepted %f %f\n",oldllhood,p->tree->ll);

                if (p->tree->left->n > p->tree->right->n) {
                    Tree * s=p->tree->left;
                    p->tree->left=p->tree->right;
                    p->tree->right=s;
                };
                gsl_vector_char_free(ancSeq);
                gsl_vector_char_free(recMap);
                gsl_vector_char_free(recMapx);
                gsl_vector_char_free(recMapy);
                gsl_vector_char_free(recRoot);
                gsl_vector_char_free(recMapxbro);
            }
            p->tree->updatellgivenllb();
            free(ys);
            free(probys);
            if (nbswaps==0) {
                gettimeofday(&tv,0);
                tcur=tv.tv_sec*1000000+tv.tv_usec;
                if (tcur>tstop) break;
            }

            //Check that the final configuration has the right ll
            /*double ll1=p->tree->ll;
double ll2=p->tree->llhood(p);
if (fabs(ll1-ll2)>0.0001) {printf("error1 %f %f %f\n",ll1,ll2,oldllhood);exit(0);}
if (x->recMap==recMapx && fabs(ll1-oldllhood)>0.0001) {printf("error2 %f %f %f\n",ll1,ll2,oldllhood);exit(0);}*/

        }
        if (p->verbose) printf("Performed %d branch-swapping attempts\n",repeats);
        gettimeofday(&tv,0);
        tlast=tv.tv_sec*1000000+tv.tv_usec;
    }

}
