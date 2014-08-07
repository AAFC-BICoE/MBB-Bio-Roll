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
#include "alignment.h"

namespace wb {

    Alignment::Alignment() {
        polySites=NULL;
        data=NULL;
        consensus=NULL;
        for (int i=0;i<10000;i++) names[i]=NULL;
        setN(0);
        setL(0);
    }

    Alignment::Alignment(int N,int L) {
        polySites=NULL;
        consensus=NULL;
        data=NULL;
        for (int i=0;i<10000;i++) names[i]=NULL;
        this->N=N;
        this->L=L;
        resetData();
    }

    void Alignment::resetData() {
        if (data!=NULL)
            gsl_matrix_char_free(data);
        if (N>0 && L>0)
            data=gsl_matrix_char_calloc(N,L);
        else
            data=NULL;
    }

    Alignment::~Alignment() {
        for (int i=0;i<N;i++) if (names[i]!=NULL) free(names[i]);
        if (consensus!=NULL)
            gsl_vector_char_free(consensus);
        if (data!=NULL)
            gsl_matrix_char_free(data);
        if (polySites!=NULL)
            gsl_vector_int_free(polySites);
    }


    void Alignment::setN(int N) {
        this->N=N;
        resetData();
    }
    /*
int Alignment::getN()
{
    return N;
}*/

    void Alignment::setL(int L) {
        this->L=L;
        resetData();
    }
    /*
int Alignment::getL()
{
    return L;
}*/

    void Alignment::setData(int i,int j,char value) {
        gsl_matrix_char_set(data,i,j,value);
    }

    char Alignment::getData(int i,int j) {
        return gsl_matrix_char_get(data,i,j);
    }

    void Alignment::cleanUp() {
        printf("Cleaning-up the alignment...\n");
        gsl_vector_char * tokeep=gsl_vector_char_calloc(getL());
        //First find sites where all strains are present
        for (int i=0;i<L;i++)
        {
            int nb=0;
            for (int j=0;j<N;j++)
                if (getData(j,i)!=UNLINKED && getData(j,i)!='N') nb++;
            if (nb>=N) gsl_vector_char_set(tokeep,i,1);
        }

        for (int i=0;i<L;i++)
        {
            //non-keeping site -> don't keep
            if (gsl_vector_char_get(tokeep,i)==0) continue;
            //keeping site in a keeping region -> keep
            if (i>0 && gsl_vector_char_get(tokeep,i-1)==1 && gsl_vector_char_get(tokeep,i)==1) continue;
            //keeping site in a non-keeping region -> keep only if 1000 keeping sites follow
            int k=0;
            for (int j=i;j<i+1000 && j<L;j++) {if (gsl_vector_char_get(tokeep,j)==1) k++;if (getData(0,j)==UNLINKED) {k=0;break;}}
            if (k<1000) gsl_vector_char_set(tokeep,i,0);
        }
        int l=0;
        for (int i=0;i<L;i++)
        {
            if (gsl_vector_char_get(tokeep,i)==1 && l>0 && gsl_vector_char_get(tokeep,i-1)==0) l++;
            if (gsl_vector_char_get(tokeep,i)==1) l++;
        }
        gsl_matrix_char * dat=gsl_matrix_char_alloc(N,l);
        int pos=0;
        for (int i=0;i<L;i++)
            if (gsl_vector_char_get(tokeep,i)==1) {
            if (pos>0 && gsl_vector_char_get(tokeep,i-1)==0) {for (int j=0;j<N;j++) gsl_matrix_char_set(dat,j,pos,UNLINKED);pos++;}
            for (int j=0;j<N;j++) gsl_matrix_char_set(dat,j,pos,getData(j,i));
            pos++;
        }
        setL(l);
        gsl_matrix_char_free(data);
        data=dat;
        gsl_vector_char_free(tokeep);
        makePolySites();
        printf("N=%d, b=%d, L=%d\n",N,getB(),L);
    }

    void Alignment::makePolySites() {
        if (polySites!=NULL)
            gsl_vector_int_free(polySites);
        int eq;
        int nb=0;
        for (int i=0;i<L;i++) {
            eq=1;
            for (int j=0;j<N-1;j++)
                if (getData(j,i)!=getData(j+1,i) || getData(j,i)=='N' || getData(j+1,i)=='N')
                    eq=0;
            if (eq==0 || getData(0,i)==UNLINKED || i==L-1 || (i>0 && getData(0,i-1)==UNLINKED) || (i<L-1 && getData(0,i+1)==UNLINKED) || i%mindistrefsites==0)
                nb++;
        }


        polySites=gsl_vector_int_calloc(nb);
        nb=0;

        for (int i=0;i<L;i++) {
            eq=1;
            for (int j=0;j<N-1;j++)
                if (getData(j,i)!=getData(j+1,i) || getData(j,i)=='N' || getData(j+1,i)=='N')
                    eq=0;
            if (eq==0 || getData(0,i)==UNLINKED || i==L-1 || (i>0 && getData(0,i-1)==UNLINKED) || (i<L-1 && getData(0,i+1)==UNLINKED) || i%mindistrefsites==0)
                gsl_vector_int_set(polySites,nb++,i);
        }
        printf("Using %d reference sites\n",nb);
        //for (int i=0;i<nb;i++)
        //printf("%d\n",gsl_vector_int_get(polySites,i));

        //Make the consensus sequence
        consensus=gsl_vector_char_calloc(L);
        for (int i=0;i<L;i++) {
            int cpt[5]={0,0,0,0,0};
            for (int s=0;s<N;s++)
                switch (getData(s,i)) {
                case '0':cpt[0]++;break;
                case '1':cpt[1]++;break;
                case '2':cpt[2]++;break;
                case '3':cpt[3]++;break;
                case UNLINKED:cpt[4]++;break;
                }
            int w;
            if (cpt[4]>0) w=UNLINKED; else
            {
                w='0';
                if (cpt[1]>cpt[0] && cpt[1]>cpt[2] && cpt[1]>cpt[3]) w='1';
                if (cpt[2]>cpt[0] && cpt[2]>cpt[1] && cpt[2]>cpt[3]) w='2';
                if (cpt[3]>cpt[0] && cpt[3]>cpt[1] && cpt[3]>cpt[2]) w='3';
            }
            gsl_vector_char_set(consensus,i,w);
        }
    }

    double Alignment::diff(gsl_vector_char * a,gsl_vector_char * b){
        double d=0.0;
        for (unsigned int i=0;i<polySites->size;i++)
            if (gsl_vector_char_get(a,gsl_vector_int_get(polySites,i))!=
                gsl_vector_char_get(b,gsl_vector_int_get(polySites,i))) d++;
        return d;
    }

    double Alignment::diff2(gsl_vector_char*a,gsl_vector_char*b){
        return 1.0;
        double d=0.0;
        int prev=-10000;
        for (unsigned int i=0;i<polySites->size;i++)
            if (gsl_vector_char_get(a,gsl_vector_int_get(polySites,i))!=
                gsl_vector_char_get(b,gsl_vector_int_get(polySites,i)))
            {
            double add=GSL_MIN(1.0,(gsl_vector_int_get(polySites,i)-prev)/500.0);
            if (add<=0.0) add=1.0;
            d+=add;
            prev=gsl_vector_int_get(polySites,i);
        }
        return d;
    }

    void Alignment::removeGaps(bool onlyNonPoly) {
        //Replace alignments gaps with highest frequency nucleotide
        gsl_vector_int * freqs=gsl_vector_int_calloc(4);
        for (int i=0;i<getL();i++)
            for (int j=0;j<getN();j++)
                if (getData(j,i)=='N') {
            for (int k=0;k<4;k++) gsl_vector_int_set(freqs,k,0);
            for (int k=0;k<getN();k++) if (getData(k,i)-'0'<4) (*gsl_vector_int_ptr(freqs,getData(k,i)-'0'))++;
            if (!onlyNonPoly || gsl_vector_int_max(freqs)==gsl_vector_int_get(freqs,0)+gsl_vector_int_get(freqs,1)+gsl_vector_int_get(freqs,2)+gsl_vector_int_get(freqs,3))
                setData(j,i,gsl_vector_int_max_index(freqs)+'0');
        }
        makePolySites();
    }

    int Alignment::getB() {
        int b=1;
        for (int i=0;i<L;i++) if (getData(0,i)==UNLINKED) b++;
        return b;
    }

    void Alignment::writeToFile(char * filename) {
        printf("Writing alignment to file %s...\n",filename);
        char * lets="ATCG";
        char * buf=(char*)malloc(getL()+5);
        FILE * f=fopen(filename,"w");
        int beg=0;
        int end=0;
        for (unsigned int i=0;i<getB();i++) {
            end=beg;while (end<getL() && getData(0,end)!=UNLINKED) end++;
            for (unsigned int j=0;j<getN();j++) {
                for (unsigned int k=beg;k<end;k++)
                    if (getData(j,k)=='N') memcpy(buf+k-beg,"-",1);else memcpy(buf+k-beg,lets+getData(j,k)-'0',1);
                sprintf(buf+end-beg,"\0");
                fprintf(f,"> %s\n%s\n",names[j],buf);
            }
            fprintf(f,"=\n");
            beg=end+1;
        }
        fclose(f);
        free(buf);
    }

}
