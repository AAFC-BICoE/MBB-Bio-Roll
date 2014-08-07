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
#ifndef WBTREE_NEWICK_H
#define WBTREE_NEWICK_H

#include <tree.h>
#include <fstream>
#include <sstream>
#include <string>
#include "param.h"

using namespace std;

namespace wb {

    /**
@brief Class to read a Newick file
@author Xavier Didelot
*/
    class Tree_newick : public Tree
    {
    public:
        Tree_newick();
        Tree_newick(Param * p,Tree *** where,char * name);///<Creates a new phylogeny adapted to the given parameters
        ~Tree_newick();
        void init_newick(string *str,Tree*father,Tree *** where,int N);
        void doAges();

    };

}

#endif
