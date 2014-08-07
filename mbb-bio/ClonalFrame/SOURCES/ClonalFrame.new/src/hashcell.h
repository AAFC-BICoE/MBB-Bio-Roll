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
#ifndef WBHASHCELL_H
#define WBHASHCELL_H
#include "param.h"

namespace wb {

    /**
@brief A cell of the hash table used in the generation of consensus trees
@author Xavier Didelot
*/
    class HashCell{
    public:
        HashCell(bool * id,Param * p);
        ~HashCell();
        void addNode(Tree * t);
        bool * id;
        int nb;
        double age;
        double ageabove;
        gsl_vector * recs;
        gsl_vector * muts;
        HashCell * next;
        Param * p;
    };
}

#endif
