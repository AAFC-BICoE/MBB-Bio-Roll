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
#ifndef WBCONSENSUS_H
#define WBCONSENSUS_H
#include "tree.h"
#include "param.h"
#include "hashcell.h"
#include "param.h"
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_randist.h>

namespace wb {

    class HashCell;

    /**
@brief Creates a majority-rule consensus tree
@author Xavier Didelot
*/
    class Consensus{
    public:
        Consensus(Param * p,int t);
        void addTree(Tree * t);
        char * retConsensus(double cutoff);
        ~Consensus();
        Tree ** where;
        HashCell ** tokeep;
        int nbtokeep;
        int sum(bool*a);
        void addNode(Tree * t);
    protected:
        HashCell ** hashTable;
        int n;///<Number of taxons per tree
        int t;///<Number of trees
        Param * p;
        bool * calid(Tree * t);
        int hash(bool * id);
        gsl_vector_int * a;
        bool eq(bool*a,bool*b);
        bool incl(bool*a,bool*b);
        void minus(bool*a,bool*b);
        bool* copy(bool *a);
        void ad(bool * res,Tree * t);
        int first(bool*a);
        char * buildsubtree(int w,HashCell ** tokeep,int nbtokeep);
    };


}
#endif
