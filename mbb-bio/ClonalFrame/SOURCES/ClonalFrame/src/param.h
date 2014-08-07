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
#ifndef STDPARAM_H
#define STDPARAM_H

#include "alignment.h"
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_randist.h>
#include "genes.h"
#include "tree.h"
#include "util.h"
#include "tree_coal.h"
#include "tree_simple.h"
#include "tree_upgma.h"
#include "tree_newick.h"

namespace wb {

    class Move;
    class Recorder;

    /**
@brief This represents the parameters of the model
@author Xavier Didelot
*/
    class Param{
    public:
        Param(Alignment * a,gsl_rng * rng,int treeinit);///<Creates a new set of parameters
        ~Param();///<Class destructor
        Alignment * a;///<Alignment for which the parameters were created
        void init(double mu,double delta,double nu,double rho);///<Randomly initialize all the parameters
        gsl_rng * rng;///<Random number generator
        Tree * tree;///<Phylogeny of the sequences in the alignment
        void metropolis(Move ** m,int nbMoves,int nbIters,int burnin,int thining,char * out);///<Performs the Metropolis-Hastings algorithm
        void loadNewick(char * name);///<Load a Newick tree
        double mu;///<Mutational parameter
        double rho;///<Inverse of the expected size of a non recombinant segment
        double delta;///<Inverse of the expected size of a recombinant segment
        double nu;///<Mutational rate in imported regions
        Tree ** where;
        Recorder * recorder;
        bool uniprior;
        bool verbose;
        bool fastcf;
        double nubeta1;
        double nubeta2;
        double thetabase;
        double Rbase;
        double deltabase;
        double expgrowth;
        gsl_vector_char * cf;
        int rec,mut,mutrec;
    };

}

#endif
