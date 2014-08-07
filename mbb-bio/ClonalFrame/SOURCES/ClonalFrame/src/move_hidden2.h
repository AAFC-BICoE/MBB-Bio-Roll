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
#ifndef WBMOVE_HIDDEN2_H
#define WBMOVE_HIDDEN2_H

#include <move.h>
#include "move_hidden.h"

namespace wb {

    /**
@brief Move that encapsulates Move_hidden within a Metropolis-Hastings move
This move calculates the Metropolis-Hastings ratio and accept the proposed Move_hidden depending on it.
This is only useful for verification of the Move_hidden class.
@author Xavier Didelot
*/
    class Move_hidden2 : public Move
    {
    public:
        Move_hidden2(gsl_rng * rng,Param * p);
        Move_hidden * mh;
        ~Move_hidden2();
        void move(Param *p);///<Execute the move on the given parameters

    };

}

#endif
