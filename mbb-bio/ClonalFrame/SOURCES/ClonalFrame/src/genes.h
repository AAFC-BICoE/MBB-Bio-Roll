/***************************************************************************
 *   Copyright (C) 2011 by Xavier Didelot   *
 *   xavier.xavier.didelot@gmail.com   *
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
#ifndef STDGENES_H
#define STDGENES_H
#include <gsl/gsl_matrix.h>
#include "alignment.h"

namespace wb {

    /**
@brief This class represents a genetic map of a genome
@author Xavier Didelot
*/
    class Genes{
    public:
        /**
     * Creates the genetic map
     * @param a Alignment on which the genetic map is based
     * @param mapfile This file contains a non genetic map of the genomes in the alignment
     * @param genesfile This file contains the real location of the genes
     * @return A genetic map corresponding to the input files
     */
        Genes(Alignment *a,char * mapfile,char * genesfile);
        ~Genes();///<Class destructor
        gsl_vector_int ** locs;///<Locations of the genes in the alignment
        int nbgenes;///<Number of genes in the genetic map
    };

}

#endif
