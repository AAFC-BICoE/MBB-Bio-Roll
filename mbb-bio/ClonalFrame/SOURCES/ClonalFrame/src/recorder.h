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
#ifndef WBRECORDER_H
#define WBRECORDER_H
#include <gsl/gsl_matrix.h>
#include "param.h"
#include "consensus.h"

namespace wb {

    /**
@brief Records the current state of the MCMC, and output a summury at the end
@author Xavier Didelot
*/
    class Recorder{
    public:
        Param * p;
        Recorder(Param *p,int nbIters,int burnin,int thining);
        void record(int it);///<Record the current state of the chain after the burnin
        void recordBurnin(int it);///<Record the current state of the chain dur
        ~Recorder();
        void saveResults(char * out,double cutoff);///<Save all the results in files starting with the given prefix
        Consensus * consensus;
    protected:
        int nbIters;
        int burnin;
        int thining;
        gsl_matrix * resultsRecMap;///<Record of the recombinant map for each sequence
        gsl_matrix * resultsMutMap;///<Record of the location of mutations for each sequence
        gsl_matrix * resultsAncSeq;///<Record of the ancestral sequences for each node of the tree
        gsl_vector * resultsLlhood;///<Record of the log likelihood of the current state
        gsl_vector * resultsNu;///<Record of the values of nu
        gsl_vector * resultsMu;///<Record of the values of mu
        gsl_vector * resultsDelta;
        gsl_vector * resultsRho;
        char ** resultsPhylo; ///<Record of how often each possible phylogeny is used
    };

}

#endif
