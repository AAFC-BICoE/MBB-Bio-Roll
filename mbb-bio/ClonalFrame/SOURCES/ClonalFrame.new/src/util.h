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
#ifndef STDUTIL_H
#define STDUTIL_H

#include <gsl/gsl_matrix.h>
#include <stdio.h>
#include "math.h"
#include <gsl/gsl_sf_log.h>
//#include <fstream>

namespace wb {

    /**
@brief This class only contains static utilitary methods
@author Xavier Didelot
*/
    class Util{
    public:
        /**
     * Prints a matrix to a file
     * @param filename Name of the file to which to print
     * @param mat Matrix to print
     */
        static void mat2file(char * filename,gsl_matrix * mat);

        /**
     * Prints a vector to a file
     * @param filename Name of the file to which to print
     * @param vec Vector to print
     */
        static void vec2file(char * filename,gsl_vector * vec);

        /**
      * Normalize a vector
      * @param v Vector to normalize
      */
        static void vec2file(FILE * f,gsl_vector * vec);
        static void normalize(gsl_vector * v);
        static void normalize(double *v,int size);
        static int  vecsum_char(gsl_vector_char * vec);
        static double lBinoProb (int i,int n, double p);
        static double lbetapdf(double x,double a,double b);
        static double mylgamma(double z);
        static double LDirichletProb(double prior[],double post[],int length);
    };
}

/*    inline static bool in(int x,gsl_vector_int * y) {
for (unsigned int i=0;i<y->size;i++) if (gsl_vector_int_get(y,i)==x) return true;
return false;
}
*/
#endif
