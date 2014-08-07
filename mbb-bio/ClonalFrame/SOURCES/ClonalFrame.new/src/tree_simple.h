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
#ifndef WBTREE_SIMPLE_H
#define WBTREE_SIMPLE_H

#include <tree.h>
#include "param.h"


namespace wb {

    /**
@brief This class represents a node of a phylogenic tree initially equal to (1,(2,(3,...)))
@author Xavier Didelot
*/
    class Tree_simple : public Tree
    {
    public:
        Tree_simple(Param * p,Tree *** where);///<Creates a new phylogeny adapted to the given parameters
        Tree_simple(Param * p,int n,Tree * father);///<Create a new node of the phylogenic tree who has n terminal children and whose father is given
        void init(Param * p,int n);///<Initialisation of a node of the phylogeny
        ~Tree_simple();

    };

}

#endif
