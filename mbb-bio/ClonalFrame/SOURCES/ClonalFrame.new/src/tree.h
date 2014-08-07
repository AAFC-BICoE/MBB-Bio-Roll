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
#ifndef STDTREE_H
#define STDTREE_H
#include "stdlib.h"
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_math.h>
#include <gsl/gsl_sf_log.h>
#include <gsl/gsl_sort_vector.h>
#include <gsl/gsl_sf_exp.h>
#include <string.h>

namespace wb {

    class Param;

    /**
@brief This class represents a node of a phylogenic tree
@author Xavier Didelot
*/
    class Tree{
    public:
        Tree();///<Creates an empty node
        ~Tree();///<Destructor of a node
        double age;///<Age of the node
        Tree * left;///<Left child of a node
        Tree * right;///<Right child of a node
        Tree * father;///<Father of a node
        gsl_vector_char * ancSeq;///<Ancestral sequence associated to this node
        gsl_vector_char * recMap;///<Recombination map associated to this node
        Tree ** nodes;///<List of internal nodes equal to or under the current node
        int n;///<Number of sequences for which the tree is built
        int id;///<Used only for leaves, indicates the number of the sequence the leaf corresponds to
        static Tree * move(Tree * x,Tree * y,double newAge,gsl_vector_char * ancSeq,gsl_vector_char * recMap,Param * p);///<Move the non-root node x under the father of y, at the given age and using the given ancestral sequence and recombination map for the intermediate node. Returns the new root to the tree.
        void updateNodes();///<Update the members n and nodes for all the nodes under this node
        double llhoodb(Param * p);///<Calculates the log-likelihood of a branch
        double llhood(Param * p);///<Calculates the log-likelihood of a tree
        double llhoodT(Param * p);
        void updatellgivenllb();
        double llb;///<Stores the log-likelihood of the branch
        double ll;///<Stores the log-likelihood of the tree
        double oldll;///<Stores the previous value of the ll of the tree
        double oldllb;///<Stores the previous value of the ll of the branch
        void reverseall();///<Replaces all ll with oldll and all llb wih oldllb in the tree
        char * newick(Tree ** where,Tree ** nodes,int * min);///<Returns the newick string representation of the tree with the additional convention that on an internal node, the child that contains the lowest leaf is placed at the left
        void ungap(gsl_vector_char * seq,Param * p);
        void fixtimes(double tottime);
        double depth();
        void count(Param * p,double * mut,double * rec,double * mutrec,gsl_vector_char * cf);///<Counts the number of rec, mut and mutrec events, as well as the proportion of clonal frame
        void countInterIntra(Param *p,int *mutin,int *mutout,int *recin,int *recout);///<Counts the number of mutations inter and intra, and the number of substitutions introduced by recombination which are inter and intra
    };
}

#endif
