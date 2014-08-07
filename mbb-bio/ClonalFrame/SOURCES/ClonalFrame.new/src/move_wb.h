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
#ifndef STDMOVE_WB_H
#define STDMOVE_WB_H

#include <move.h>
#include "move_hidden.h"
#include <sys/time.h>

namespace wb {

    /**
@brief Performs the branch swapping algorithm
@author Xavier Didelot
*/
    class Move_wb : public Move
    {
    public:

        /**
     * Creates a new instance of the class Move_wb
     * @param rng random number generator to use when performing the branch swapping algorithm
     * @param p parameters for which the Move_wb is created
     */
        Move_wb(gsl_rng* rng,Param * p);

        /**
     * Destructor of the Move_wb class
     */
        ~Move_wb();
        /**
     * Performs the branch swapping algorithm
     * @param p Parameter on which to perform the branch swapping algorithm
     */
        void move(Param* p);

	void setNbswaps(int theValue) {
	    nbswaps = theValue;
	}
	
    protected:
        Move_hidden * mh;///<Instance of the move_hidden class used to update the recombination maps and ancestral sequences necessary to calculate the acceptance probability of the branch swapping move
        int propLocs(Tree ** ys,double* probys,Tree * x,Param * p);
        int which;
        int nbswaps;
        unsigned int tlast;
    };

}

#endif
