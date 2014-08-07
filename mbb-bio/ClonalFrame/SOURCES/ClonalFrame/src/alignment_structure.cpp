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
#include "alignment_structure.h"

namespace wb
{

    Alignment_structure::Alignment_structure(char * filename,int mindistrefsites)
        : Alignment()
    {
        this->mindistrefsites=mindistrefsites;
        FILE * f=fopen(filename,"r");
        if (f==NULL) {printf("Unable to read alignment\n");abort();}

        //printf(" First count the number of lines\n");fflush(0);
        char  ch;
        bool endLine=true;
        int   numLines = 0;
        while
                (!feof(f))
        {
            ch=fgetc(f);
            if (ch == '\n')
            {
                numLines++;
                endLine=true;
            };
            if (ch>='0' & ch<='9')
            {
                endLine=false;
            };
        }
        if (endLine==false)
            numLines++;

        //printf(" Then count the number of elements\n");fflush(0);
        rewind(f);
        int buf;
        int numInts=0;
        int numBreaks=-1;
        while (!feof(f))
        {
            if (fscanf(f,"%d",&buf)>0)
            {//printf("%d %d\n",numInts,numBreaks);fflush(0);
                numInts++;
                if (buf==-1)
                    numBreaks++;
            }
        }

        //printf(" Then read the data into an integer matrix\n");fflush(0);
        rewind(f);
        gsl_matrix_int * d=gsl_matrix_int_calloc(numLines,numInts/numLines);
        gsl_matrix_int_fscanf(f,d);

        //printf("Makes sure that the values start from 0\n");
        gsl_matrix_int_view v=gsl_matrix_int_submatrix(d,1,0,numLines-1,numInts/numLines);
        int min=gsl_matrix_int_min(&(v.matrix));
        //printf("Minimum found:%d\n",min);
        gsl_matrix_int_add_constant(&(v.matrix),-min);
        //v=gsl_matrix_int_submatrix(d,1,0,numLines-1,numInts/numLines);
        //min=gsl_matrix_int_min(&(v.matrix));
        //printf("Minimum now:%d\n",min);

        //printf(" Then create the data matrix\n");fflush(0);
        if (data!=NULL)
            gsl_matrix_char_free(data);
        int sum=0;
        for (int i=0;i<numInts/numLines;i++)
            sum+=abs(gsl_matrix_int_get(d,0,i));
        setL(sum);////+numBreaks);
        setN(numLines-1);

        for (int i=0;i<numLines-1;i++) {names[i]=(char*)calloc(100,sizeof(char));sprintf(names[i],"%d",i+1);}
        int pos=-1;
        char *c=(char *)calloc(10,sizeof(char));

        for (int i=0;i<sum;i++)
            for (int j=0;j<numLines-1;j++)
                gsl_matrix_char_set(data,j,i,'0');

        for (int i=0;i<numInts/numLines;i++)
        {
            pos+=abs(gsl_matrix_int_get(d,0,i));
            for (int j=1;j<numLines;j++)
            {
                sprintf(c,"%d",gsl_matrix_int_get(d,j,i));
                gsl_matrix_char_set(data,j-1,pos,*c);
            }
            if (gsl_matrix_int_get(d,0,i)==-1 && pos>0)
            {
                ////pos++;
                for (int j=1;j<numLines;j++)
                {
                    ////gsl_matrix_char_set(data,j-1,pos,gsl_matrix_char_get(data,j-1,pos-1));
                    gsl_matrix_char_set(data,j-1,pos-1,UNLINKED);
                }
            }
        }
        free(c);

        gsl_matrix_int_free(d);
        fclose(f);

        //    for (int i=0;i<getN();i++) {
        //for (int j=0;j<getL();j++) printf("%c ",gsl_matrix_char_get(data,i,j));
        //printf("\n");
        //}

        makePolySites();

        map=gsl_vector_int_calloc(getL());
        gsl_vector_int_set(map,0,0);
        for (int i=1;i<getL();i++) gsl_vector_int_set(map,i,gsl_vector_int_get(map,i-1)+1);
    }

    Alignment_structure::~Alignment_structure()
    {
        gsl_vector_int_free(map);
    }

    void Alignment_structure::makeMap(char * filename)
    {
        FILE * f=fopen(filename,"r");
        gsl_vector_int_fscanf(f,map);
        fclose(f);
    }
}
