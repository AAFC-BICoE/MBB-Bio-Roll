/***************************************************************************
 *   Copyright (C) 2011 by Xavier Didelot   *
 *   xavier.xavier.didelot@gmail.com   *
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
#ifndef STDMOVE_HIDDEN_H
#define STDMOVE_HIDDEN_H

#include <move.h>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_blas.h>

namespace wb {

    /**
@brief Update of the ancestral sequences of all internal nodes and recombination maps of all non-root nodes
@author Xavier Didelot
*/
    class Move_hidden : public Move
    {
    public:
        Move_hidden(gsl_rng * rng,Param * p);///<Creates an instance of the class using the given random number generator
        ~Move_hidden();///<Class destructor
        void move(Param *p);///<Execute the move on the given parameters
        void move1(Param *p,Tree * t);
        void forwardfast(Param *p,Tree *t);///<fastClonalFrame version of forward+backward
        double pprop;
        bool calculMode;
    protected:
        gsl_matrix * a;///<Transition matrix
        gsl_matrix * e;///<Emission matrix
        gsl_vector * pbeg;
        double *** q;///<Matrix q
        gsl_matrix * forward(Param *p);///<Forward algorithm
        void backward(Param *p,gsl_matrix * f,Tree * t);///<Backward algorithm
        int setState (Tree * t,Param * p,int site,gsl_vector * probas);
        void setState2(Tree * t,Param * p,int site,int j);
        int nbstates;///<Number of different possible hidden states of the HMM
        int nbmsgs;///<Number of different possible emitted messages of the HMM
        void makea(Param * p,Tree * t);///<Creates the transition matrix
        void makee(Param * p,Tree * t);///<Creates the emission matrix
        void makeq(int maxDist);///<Creates the matrix q
        char drawSeq(Param * p,Tree * t,int i);///<Returns a new randomly chosen ancestral sequence character for the i-th locus of the non-root node t
        char * msgs;///<Messages emitted by the HMM
        void makeMsgs (Tree *t);///<Creates the messages emitted by the HMM for an internal non-root node
        void makeMsgsroot(Tree * t);///<Creates the messages emitted by the HMM for the root
        void makepbeg(Param * p,Tree *t);
        void fillgap(Tree *t,Param *p,int a,int b,int x,int y);
    };

}

#endif
