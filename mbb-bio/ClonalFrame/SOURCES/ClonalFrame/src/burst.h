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
#ifndef WBBURST_H
#define WBBURST_H

#include <gsl/gsl_matrix.h>
#include "alignment.h"
#include "util.h"
#include "hashcell.h"
#include "consensus.h"
#include "recorder.h"
#include <vector>

using namespace std;

namespace wb {

    /**
@brief This class performs the BURST algorithm
@author Xavier Didelot
*/
    class Burst{
    public:
        Burst(Alignment * a);
        ~Burst();
        gsl_matrix_char * data;
        gsl_matrix_char * typize(Alignment * a);///<Create the MLST data given the alignment
        void burst(Param * p);///<Performs the BURST algorithm and put the output in the recorder of p
        vector<vector<int> > * splitGroups();///<Splits the data into BURST groups (where any two elements of a group are connected through a chain of Single Locus Variants)
        vector<vector<int> > * sortGroup(vector<int> v);///<Takes the list of element of a BURST group, and returns the list of subgroups, in descendent order of inclusion (ie. start with largest, finish with smallest group)
        int diff(int a,int b);///<Returns the number of differences between STs a and b
        vector<vector<int> > * ridDoubles(vector<int> v);///<Identify the duplicate in a list of STs: the first vector returned is the list without the replicates whereas the rest of the output are lists of identical STs
        void makeFathers(gsl_vector_int * fathers,vector<vector<int> > *slvs,int f);///<Assigns the fathers of each ST given the list of SLV relationship and the founder of group f
        void optimiseFathers(gsl_vector_int * fathers,vector<vector<int> > *slvs,int f);///<Optimise the fathers of each ST given the list of SLV relationship and the founder of group f
        vector<vector<int> > * makeClusters(vector<int> *v,gsl_vector_int * fathers,int f,bool top);///<Create the subgroups corresponding to a given topology of a group
        bool descended(int which,int orig,gsl_vector_int * fathers);///<Returns true if which is descended from orig according to fathers, and false otherwise
    };

}

#endif
