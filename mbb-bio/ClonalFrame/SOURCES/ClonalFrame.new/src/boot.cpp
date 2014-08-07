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
#include "boot.h"

namespace wb {

    Boot::Boot(Alignment * a,bool genebygene) {
        this->a=a;
        this->genebygene=genebygene;
    }


    Boot::~Boot() {}

    void Boot::boot(Param * p) {
        //Reset the consensus tree of the recorder of p
        delete(p->recorder->consensus);
        Consensus * cons=new Consensus(p,2000);
        p->recorder->consensus=cons;
        Tree ** where;
        //Add the UPGMA tree 1000 times
        Tree_UPGMA * t=new Tree_UPGMA(p,&where);
        for (int i=0;i<1000;i++)
            cons->addTree(t);
        for (int i=0;i<a->getN();i++)
            delete(where[i]);
        for (int i=1;i<a->getN()-1;i++)
            delete(t->nodes[i]);
        delete t;
        free(where);
        //Add 1000 bootstrapped trees
        for (int i=0;i<1000;i++) {
            Alignment * a2;
            if (genebygene==false)
                a2=mix(p,a);
            else
                a2=mix2(p,a);
            p->a=a2;
            t=new Tree_UPGMA(p,&where);
            cons->addTree(t);
            for (int i=0;i<a->getN();i++)
                delete(where[i]);
            for (int i=1;i<a->getN()-1;i++)
                delete(t->nodes[i]);
            delete t;
            free(where);
            delete a2;
        }
        p->a=a;
    }

    Alignment * Boot::mix(Param * p,Alignment * a) {
        int tocopy;
        Alignment * a2=new Alignment(a->getN(),a->getL());
        for (int i=0;i<a->getL();i++) {
            //For each size i, copy a randomly chosen site (with replacement)
            if (a->getData(0,i)==UNLINKED)
                tocopy=i;
            else
                tocopy=gsl_rng_uniform_int(p->rng,a->getL());
            for (int j=0;j<a->getN();j++)
                a2->setData(j,i,a->getData(j,tocopy));
            //printf("%c%c%c\n",a2->getData(0,i),a2->getData(1,i),a2->getData(2,i));
        }
        a2->makePolySites();
        return a2;
    }

    Alignment * Boot::mix2(Param * p,Alignment * a) {
        //Count number of fragments
        vector<int> * frags=new vector<int>;
        frags->push_back(-1);
        for (unsigned int i=0;i<a->polySites->size;i++)
            if (a->getData(0,gsl_vector_int_get(a->polySites,i))==UNLINKED)
                frags->push_back(gsl_vector_int_get(a->polySites,i));
        frags->push_back(a->getL());
        //Choose fragments with replacement
        gsl_vector_int * frags2=gsl_vector_int_calloc(frags->size()-1);
        for (unsigned int i=0;i<frags2->size;i++)
            gsl_vector_int_set(frags2,i,gsl_rng_uniform_int(p->rng,frags2->size));
        //Calculate length of new alignment
        int size=frags2->size-1;
        for (unsigned int i=0;i<frags2->size;i++)
            size+=frags->at(gsl_vector_int_get(frags2,i)+1)-frags->at(gsl_vector_int_get(frags2,i))-1;
        Alignment * a2=new Alignment(a->getN(),size);
        //Fill up
        int pos=0;
        //For each fragment
        for (unsigned int i=0;i<frags2->size;i++) {
            //For each site of the fragment to copy
            for (int j=frags->at(gsl_vector_int_get(frags2,i))+1;j<frags->at(gsl_vector_int_get(frags2,i)+1);j++) {
                //Copy for all individuals
                for (int k=0;k<a->getN();k++)
                    a2->setData(k,pos,a->getData(k,j));
                pos++;
            }
            //Add UNLINKED if needed
            if (i+1<frags2->size) for (int k=0;k<a->getN();k++) a2->setData(k,pos,UNLINKED);
            pos++;
        }

        delete frags;
        gsl_vector_int_free(frags2);
        a2->makePolySites();
        return a2;
    }

}
