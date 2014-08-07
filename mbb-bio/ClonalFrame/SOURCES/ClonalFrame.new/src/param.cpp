/***************************************************************************
 *   Copyright (C) 2011 by Xavier Didelot                                  *
 *   xavier.didelot@gmail.com                                                  *
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
#include "param.h"
#include "move.h"
#include "recorder.h"

namespace wb {

    Param::Param(Alignment * a,gsl_rng * rng,int treeinit) {
        verbose=false;
        this->a=a;
        this->rng=rng;
        Tree ** where;
        if (treeinit==0) this->tree=new Tree_simple(this,&where);
        if (treeinit==1) this->tree=new Tree_coal  (this,&where);
        if (treeinit==2) this->tree=new Tree_UPGMA (this,&where);
        this->where=where;
        uniprior=false;
        this->cf=gsl_vector_char_calloc(a->getL());
    }

    Param::~Param() {
        gsl_vector_char_free(cf);
        verbose=false;
        for (int i=0;i<a->getN();i++)
            delete(where[i]);
        for (int i=1;i<a->getN()-1;i++)
            delete(tree->nodes[i]);
        delete(tree);
        free(where);
    }

    void Param::init(double mu,double delta,double nu,double rho) {
        this->mu=mu;
        this->delta=delta;
        this->nu=nu;
        this->rho=rho;
    }

    void Param::metropolis(Move ** m,int nbMoves,int nbIters,int burnin,int thining,char * out) {
        if (nbIters<=0) {recorder=new Recorder(this,1,0,1);recorder->record(0);} else {
            recorder=new Recorder(this,nbIters,burnin,thining);
            for (int mcmc=0;mcmc<nbIters;mcmc++) {
                if (verbose) printf("Iteration %d\n",mcmc);
                //if (verbose) printf("TMRCA=%f, mu=%f, llhood=%f\n",tree->age,mu,tree->ll);
                if (!verbose) {
                    if (nbIters>50 && (mcmc)%(nbIters/50)==0)
                    {printf("\b\b\b\b\b# %3d%%",mcmc*100/nbIters);fflush(0);}
                    if (mcmc+1==nbIters) {printf("\b\b\b\b\b# 100%%\n");fflush(0);}
                }
                for (int i=0;i<nbMoves;i++) {
                    //printf("%d %d\n",gsl_vector_char_get(tree->left->recMap,5),gsl_vector_char_get(tree->right->recMap,5));
                    //printf("%s\n",tree->newick(where,tree->nodes,NULL,a->seqs));
                    //            printf("TMRCA=%f, mu=%f, llhood=%f\n",tree->age,mu,tree->ll);
                    m[i]->move(this);
                }
                if (mcmc< burnin && mcmc%thining==0) recorder->recordBurnin(mcmc);
                if (mcmc>=burnin && mcmc%thining==0) recorder->record(mcmc);
            }
        }
        recorder->saveResults(out,0.50);
        /*char buf[1000];
    sprintf(buf,"%s_1",out);
    recorder->saveResults(buf,1.00);
    sprintf(buf,"%s_0.95",out);
    recorder->saveResults(buf,0.95);*/
        delete recorder;
    }

    void Param::loadNewick(char * name)
    {
	Tree ** where;
	this->tree=new Tree_newick(this,&where,name);
	this->where=where;
    }



}
