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
#ifndef STDMOVE_H
#define STDMOVE_H

#include "alignment.h"
#include "param.h"
#include <gsl/gsl_rng.h>

namespace wb {

    /**
@brief This represents a move in a Metropolis-Hastings algorithm
@author Xavier Didelot
*/
    class Move{
    public:
        Move(gsl_rng * rng);///<Initializes the move with the given random number generator
        virtual ~Move()=0;///<Class destructor
        virtual void move(Param * p)=0;///<Performs a move on the parameters p
        gsl_rng * rng;///<Random number generator used to simulate randomness
        double priority;///<Priority of the move, which is proportional to the number of times a move will be used
    };

}

#endif
