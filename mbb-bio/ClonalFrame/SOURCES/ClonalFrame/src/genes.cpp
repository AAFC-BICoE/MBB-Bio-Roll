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
#include "genes.h"

namespace wb
{

    Genes::Genes(Alignment *a,char * mapfile,char * genesfile)
    {
        //Read in the map
        FILE * mapf=fopen(mapfile,"r");
        gsl_vector_int * map=gsl_vector_int_calloc(a->getL());
        int buf;
        for (int i=0;i<a->getL();i++)
            if (a->getData(0,i)!=UNLINKED)
            {
            fscanf(mapf,"%d",&buf);
            //printf("%d ",buf);
            gsl_vector_int_set(map,i,buf);
        }
        fclose(mapf);

        //Count the number of genes
        FILE * genes=fopen(genesfile,"r");
        int nbgene=0;
        int f1,f2,nb;
        while (fscanf(genes,"%d %d",&f1,&f2)>0)
            nbgene++;
        this->nbgenes=nbgene;
        rewind(genes);

        //Record positions of the genes
        locs=(gsl_vector_int **)calloc(nbgenes,sizeof(gsl_vector_int));
        for (int g=0;g<nbgene;g++)
        {
            fscanf(genes,"%d %d",&f1,&f2);

            nb=0;
            for (int i=0;i<a->getL();i++)
                if (gsl_vector_int_get(map,i)>=f1 && gsl_vector_int_get(map,i)<=f2)
                    nb++;
            //printf("gene %d:(%d,%d) %d\n",g,f1,f2,nb);fflush(0);
            if (nb>0)
            {
                locs[g]=gsl_vector_int_calloc(nb);
                nb=0;
                for (int i=0;i<a->getL();i++)
                    if (gsl_vector_int_get(map,i)>=f1 && gsl_vector_int_get(map,i)<=f2)
                    {
                    gsl_vector_int_set(locs[g],nb,i);
                    nb++;
                }
            } else locs[g]=NULL;
        }
        fclose(genes);
        gsl_vector_int_free(map);
    }


    Genes::~Genes()
    {
        for (int i=0;i<nbgenes;i++) if (locs[i]!=NULL) gsl_vector_int_free(locs[i]);
        free(locs);
    }


}
