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
#include "hashcell.h"

namespace wb {

    HashCell::HashCell(bool * id,Param * p)
    {
        this->id=id;
        nb=0;
        age=0.0;
        next=NULL;
        ageabove=0.0;
        recs=gsl_vector_calloc(p->a->polySites->size);
        muts=gsl_vector_calloc(p->a->polySites->size);
        this->p=p;
    }


    HashCell::~HashCell()
    {
        free(id);
        gsl_vector_free(recs);
        gsl_vector_free(muts);
        if (next!=NULL) delete(next);
    }

    void HashCell::addNode(Tree * t)
    {
        age+=t->age;
        if (t->father!=NULL) ageabove+=t->father->age;
        for (unsigned int i=0;i<GSL_MIN(p->a->polySites->size,recs->size);i++) {
            int l=gsl_vector_int_get(p->a->polySites,i);
            if (l>=t->recMap->size) break;
            *gsl_vector_ptr(recs,i)+=gsl_vector_char_get(t->recMap,l);
            if (t->father!=NULL && gsl_vector_char_get(t->ancSeq,l)!=gsl_vector_char_get(t->father->ancSeq,l))
                (*gsl_vector_ptr(muts,i))++;
        }
        nb++;
    }

}
