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
#ifndef STDALIGNMENT_STRUCTURE_H
#define STDALIGNMENT_STRUCTURE_H

#include <alignment.h>
#include <gsl/gsl_blas.h>
#include <gsl/gsl_matrix.h>

namespace wb
{

    /**
@brief This is an implementation of the class Alignment that reads the alignment from a structure file
@author Xavier Didelot
*/
    class Alignment_structure : public Alignment
    {
    public:
        /**
     * Loads the alignment contained in a structure file
     * @param filename File from which the alignment is to be read
     * @return An alignment corresponding to the structure file
     */
        Alignment_structure(char * filename,int mindistrefsites);
        ~Alignment_structure();///<Class destructor
        void makeMap(char * filename);

    };

}

#endif
