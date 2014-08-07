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
#include "tree_upgma.h"

namespace wb {

    Tree_UPGMA::Tree_UPGMA(Param * p,Tree *** where)
        : Tree() {
        //First create the initial distance matrix
        printf("UPGMA construction\n");
        int n=p->a->getN();
        father=NULL;
        ancSeq=gsl_vector_char_calloc(p->a->getL());
        recMap=gsl_vector_char_calloc(p->a->getL());
        (*where)=(Tree **)calloc(n,sizeof(Tree *));
        nodes=(Tree **)calloc(n,sizeof(Tree *));
        gsl_matrix * d=gsl_matrix_calloc(2*n,2*n);
        if (p->verbose) printf("    %d\n",n);
        for (int i=0;i<n;i++) {
            if (p->verbose) printf("iso%d     ",i);
            for (int j=0;j<n;j++) {
                double dist=0.0;
                double div=0.0;
                for (int k=0;k<p->a->getL();k++) {
                    if (p->a->getData(i,k)!='N' && p->a->getData(j,k)!='N') div++;else continue;
                    if (p->a->getData(i,k)!=p->a->getData(j,k))
                    {dist++;}
                }
                dist/=div;
                if (p->verbose) printf("%f ",dist*100);
                gsl_matrix_set(d,i,j,dist);
            }
            if (p->verbose) printf("\n");
        }

        //Create initial clusters
        int nbclusters=n;//Nb of clusters that are still to be clustered
        int * clustersid=(int *)calloc(n,sizeof(int));//List of clusters that are still to be clustered
        Tree ** clusters=(Tree **)calloc(2*n,sizeof(Tree *));//All clusters
        for (int i=0;i<n;i++) {
            clustersid[i]=i;
            clusters[i]=new Tree();
            clusters[i]->id=i;
            clusters[i]->ancSeq=gsl_vector_char_calloc(p->a->getL());
            clusters[i]->recMap=gsl_vector_char_calloc(p->a->getL());
            clusters[i]->nodes=(Tree **)calloc(n,sizeof(Tree *));
            clusters[i]->n=1;
            for (int j=0;j<p->a->getL();j++)
                gsl_vector_char_set(clusters[i]->ancSeq,j,p->a->getData(i,j));
            ungap(clusters[i]->ancSeq,p);
            (*where)[i]=clusters[i];
        }

        //Cluster all but two
        //double totage=0.0;
        while (nbclusters>2) {
            //Find smallest distance
            double min=10000.0;
            int a=-1;
            int b=-1;
            int howmany=1;
            for (int i=0;i<nbclusters;i++)
                for (int j=i+1;j<nbclusters;j++) {
                if (gsl_matrix_get(d,clustersid[i],clustersid[j])<min) {
                    min=gsl_matrix_get(d,clustersid[i],clustersid[j]);
                    a=clustersid[i];
                    b=clustersid[j];
                    howmany=1;
                }
                if (gsl_matrix_get(d,clustersid[i],clustersid[j])==min) howmany++;}
            //If more than one minimum distance, choose one at random
            if (howmany>1) {howmany=gsl_rng_uniform_int(p->rng,howmany);
                int current=0;
                for (int i=0;i<nbclusters;i++) for (int j=i+1;j<nbclusters;j++)
                    if (gsl_matrix_get(d,clustersid[i],clustersid[j])==min) {
                    a=clustersid[i];
                    b=clustersid[j];
                    if (current==howmany) goto next; else current++;
                }
            }
            //Put the two chosen cluster together in a new cluster
            next://totage+=0.5*min+gsl_rng_uniform(p->rng)/100000.0;
            Tree * t=new Tree();
            min=min+rand()/(RAND_MAX+1.0)/p->a->getL();
            t->age=0.5*min;//(min+clusters[a]->age+clusters[b]->age)/2;
            if (t->age<=clusters[a]->age) t->age=clusters[a]->age+0.5*rand()/(RAND_MAX+1.0)/p->a->getL();
            if (t->age<=clusters[b]->age) t->age=clusters[b]->age+0.5*rand()/(RAND_MAX+1.0)/p->a->getL();
            t->left=clusters[a];
            t->right=clusters[b];
            t->nodes=(Tree **)calloc(n,sizeof(Tree *));
            t->ancSeq=gsl_vector_char_calloc(p->a->getL());
            t->recMap=gsl_vector_char_calloc(p->a->getL());
            t->n=clusters[a]->n+clusters[b]->n;
            clusters[a]->father=t;
            clusters[b]->father=t;

            //Update clustersid
            int * clustersid2=(int *)calloc(n,sizeof(int));
            int j=0;
            clusters[2*n-nbclusters]=t;
            for (int i=0;i<nbclusters;i++)
                if (clustersid[i]!=a && clustersid[i]!=b)
                    clustersid2[j++]=clustersid[i];
            clustersid2[j]=2*n-nbclusters;
            free(clustersid);
            clustersid=clustersid2;

            //Update distance matrix
            for (int i=0;i<nbclusters-2;i++) {
                double dist=0.0;
                if (clustersid[i]<a) dist+=gsl_matrix_get(d,clustersid[i],a)*clusters[a]->n; else dist+=gsl_matrix_get(d,a,clustersid[i])*clusters[a]->n;
                if (clustersid[i]<b) dist+=gsl_matrix_get(d,clustersid[i],b)*clusters[b]->n; else dist+=gsl_matrix_get(d,b,clustersid[i])*clusters[b]->n;
                dist/=clusters[a]->n+clusters[b]->n;
                gsl_matrix_set(d,clustersid[i],2*n-nbclusters,dist);
            }
            nbclusters--;
        }

        //Put the two clusters under top node
        left=clusters[clustersid[0]];
        right=clusters[clustersid[1]];
        clusters[clustersid[0]]->father=this;
        clusters[clustersid[1]]->father=this;
        double min;
        if (clustersid[0]<clustersid[1]) min=gsl_matrix_get(d,clustersid[0],clustersid[1]);
        else min=gsl_matrix_get(d,clustersid[1],clustersid[0]);
        age=0.5*min;//(min+left->age+right->age)/2;
        if (age<=left ->age) age=left ->age+0.5*rand()/(RAND_MAX+1.0)/p->a->getL();
        if (age<=right->age) age=right->age+0.5*rand()/(RAND_MAX+1.0)/p->a->getL();

        //Update "nodes" and ages and create sequences for internal nodes
        updateNodes();
        for (int j=n-2;j>=0;j--)
            for (int i=0;i<p->a->getL();i++) if (gsl_rng_uniform(p->rng)<
                                                 (nodes[j]->age-nodes[j]->right->age)/(2.0*nodes[j]->age-nodes[j]->right->age-nodes[j]->left->age))
                gsl_vector_char_set(nodes[j]->ancSeq,i,gsl_vector_char_get(nodes[j]->left->ancSeq,i));
        else gsl_vector_char_set(nodes[j]->ancSeq,i,gsl_vector_char_get(nodes[j]->right->ancSeq,i));
        if (p->verbose) printf("%f\n",age);
        double totage=age;
        for (int j=n-2;j>=0;j--) nodes[j]->age=2.0*(1.0-1.0/n)*nodes[j]->age/totage;

        //Free the memory
        gsl_matrix_free(d);
        free(clustersid);
        free(clusters);
    }

    Tree_UPGMA::~Tree_UPGMA() {

    }


}
