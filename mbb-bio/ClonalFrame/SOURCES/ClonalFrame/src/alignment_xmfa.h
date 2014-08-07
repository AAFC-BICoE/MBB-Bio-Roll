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
#ifndef WBALIGNMENT_MAUVE_H
#define WBALIGNMENT_MAUVE_H

#include <alignment.h>
#include <gsl/gsl_math.h>
#include <string.h>
#include <vector>

namespace wb {

    /**
@brief This is an implementation of the class Alignment that reads the alignment from a multi-FASTA file
@author Xavier Didelot
*/
    class Alignment_xmfa : public Alignment
    {
    public:
        Alignment_xmfa(char * filename,bool ignorefirstblock,int mindistrefsites);

        ~Alignment_xmfa();

    protected:
        char convert(char in);
        void Fgets(char * buf,int l,FILE * f);
        void extractName(char * buf,char * buf2);
    };
}

#endif
