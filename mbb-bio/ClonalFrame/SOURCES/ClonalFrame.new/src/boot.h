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
#ifndef WBBOOT_H
#define WBBOOT_H
#include "alignment.h"
#include "param.h"
#include "consensus.h"
#include "recorder.h"
#include "tree_upgma.h"
#include <vector>

using namespace std;

namespace wb {

    /**
@author Xavier Didelot
*/
    class Boot{
    public:
        Boot(Alignment * a,bool genebygene);
        ~Boot();
        void boot(Param * p);
        Alignment * mix (Param * p,Alignment * a);///<Site-by-site mix of an alignment
        Alignment * mix2(Param * p,Alignment * a);///<Gene-by-gene mix of an alignment
    protected:
        Alignment * a;
        bool genebygene;
    };

}

#endif
