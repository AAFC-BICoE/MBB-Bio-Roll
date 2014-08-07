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
#ifndef STDALIGNMENT_H
#define STDALIGNMENT_H
#define UNLINKED 9

#include <gsl/gsl_matrix.h>
#include <gsl/gsl_math.h>
#include <string.h>

namespace wb
{

    /**
@author Xavier Didelot
@brief This class represents an alignment of DNA sequences
*/
    class Alignment
    {
    public:
        Alignment();///<Creates an empty alignment
        Alignment(int N,int L);///<Creates an empty alignment of N sequences of size L
        ~Alignment();///<Class destructor
        void setN(int N);///<Sets the value of N and reinitialize the data
        inline int getN() {return N;};///<Returns the value of N
        void setL(int L);///<Sets the value of L and reinitialize the data
        inline int getL() {return L;};///<Returns the value of L
        int getB();///<Returns the number of LCBs
        void setData(int i,int j,char value);///<Sets the data for the j-th position of the i-th sequence
        char getData(int i,int j);///<Gets the data for the j-th position of the i-th sequence
        void resetData();///<Creates an empty data matrix
        gsl_vector_int * polySites;///<List of polymorphic sites
        void makePolySites();///<Create the list of polymorphic sites
        gsl_vector_int * map;
        double diff(gsl_vector_char * a,gsl_vector_char * b);
        double diff2(gsl_vector_char *a,gsl_vector_char * b);
        //int seqs[1000];
        char * names[10000];
        gsl_vector_char * consensus;
        void removeGaps(bool onlyNonPoly=false);
        void writeToFile(char * filename);
        void cleanUp();
        int mindistrefsites;
    protected:
        int N;///<Number of sequences in the alignment
        int L;///<Length of the alignment
        gsl_matrix_char* data;///<The data in the alignment
    };
}

#endif
