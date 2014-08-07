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
#include "alignment_xmfa.h"

namespace wb {

    Alignment_xmfa::Alignment_xmfa(char * filename,bool ignorefirstblock,int mindistrefsites)
        : Alignment() {
        this->mindistrefsites=mindistrefsites;
        char buf[10000];
        char buf2[1000];
        //First count the number of genomes in the first LCB
        FILE * f=fopen(filename,"r");
        if (f==NULL) {printf("Unable to open input file\n");abort();}
        int nbgenomes=0;
        int i,l,j;
        int deb=0;
        while (!feof(f)) {
            Fgets(buf,10000,f);
            if (buf[0]=='>')
            {names[nbgenomes++]=(char*)calloc(1000,sizeof(char));
                extractName(buf,names[nbgenomes-1]);}
            if (buf[0]=='=' || feof(f)) break;
        }

        //Then count the number of isolates present in each of the LCBs
        std::vector<int> v;
        rewind(f);
        gsl_vector_int * check=gsl_vector_int_calloc(nbgenomes);
        if (ignorefirstblock) printf("Warning: ignoring first fragment as requested\n");
        while (!feof(f)) {
            Fgets(buf,10000,f);
            if (feof(f)) break;
            if (buf[0]=='>') {
                extractName(buf,buf2);
                for (int i=0;i<nbgenomes;i++) if (strcmp(buf2,names[i])==0) {gsl_vector_int_set(check,i,1);break;}}
            if (strncmp(buf,"=",1)==0 || feof(f)) {
                int sum=0;
                for (int i=0;i<nbgenomes;i++) sum+=gsl_vector_int_get(check,i);
                v.push_back(sum);
                if (sum<nbgenomes) {
                    int missing=0;
                    for (int i=0;i<nbgenomes;i++) if (gsl_vector_int_get(check,i)==0) {missing=i;break;}
                    printf("Warning: ignoring incomplete fragment %d (does not contain strain %s)\n",v.size(),names[missing]);
		}
                for (int i=0;i<nbgenomes;i++) gsl_vector_int_set(check,i,0);
            }
        }
        int lcb=v.size();
        gsl_vector_int_free(check);
        if (ignorefirstblock) v[0]=nbgenomes-1;

        //Then count the length of the alignment
        rewind(f);
        int length=0;
        int lcbcomplete=0;
        int lastlcomplete=0;
        for (l=0;l<lcb;l++) {
            if (v[l]<nbgenomes) {
                //Skip that fragment
                while (1) {Fgets(buf,10000,f);if (feof(f) || buf[0]=='=') break;}
                continue;
            }
            lcbcomplete++;
            lastlcomplete=l;
            while (1) {
                Fgets(buf,10000,f);
                if (buf[0]=='>')
                {extractName(buf,buf2);
                    if (strcmp(buf2,names[0])==0) break;
                }
            }
            Fgets(buf,10000,f);
            while (buf[0]!='>' && buf[0]!='=' && !feof(f)) {
                length+=strlen(buf);
                Fgets(buf,10000,f);
            }
            //Go to the end of the fragment
            while (buf[0]!='=' && ~feof(f)) {Fgets(buf,10000,f);}
        }
        printf("N=%d, b=%d, L=%d\n",nbgenomes,lcbcomplete,length);
        fclose(f);

        //Then read the data
        setL(length+lcbcomplete-1);
        setN(nbgenomes);
        map=gsl_vector_int_calloc(length+lcbcomplete-1);
        FILE ** in=(FILE **)calloc(nbgenomes,sizeof(FILE *));
        char **bufin = (char **)calloc (nbgenomes, sizeof (char *));
        int * pos=(int *)calloc(nbgenomes,sizeof(int));
        for (i=0;i<nbgenomes;i++) {
            in[i]=fopen(filename,"r");
            bufin[i] = (char*)calloc (10000, sizeof (char));
        }
        for (l=0;l<lcb;l++) {//For each LCB
            for (i=0;i<nbgenomes;i++) {//For each genome
                if (v[l]<nbgenomes) {
                    //Skip that fragment
                    while (1) {Fgets(bufin[i],10000,in[i]);if (feof(in[i]) || bufin[i][0]=='=') break;}
                    continue;
                }
                //Find next bit of alignment
                extractName(bufin[i],buf2);
                while (strcmp(names[i],buf2)!=0) {
                    Fgets(bufin[i],10000,in[i]);extractName(bufin[i],buf2);
                }
                if (i==0)
                {if (strstr(bufin[i],":")!=NULL) sscanf(strstr(bufin[i],":")+1,"%d",&deb); else deb++;}
                Fgets (bufin[i], 10000, in[i]);
                //And copy it
                while (bufin[i][0]!='>' && bufin[i][0]!='=' && !feof(in[i])) {
                    for (j=0;j<strlen(bufin[i]);j++) {
                        if (i==0 && convert(bufin[i][j])!='N')
                            gsl_vector_int_set(map,pos[i],deb++);
                        setData(i,pos[i]++,(convert(bufin[i][j])));
                    }
                    Fgets(bufin[i],10000,in[i]);
                }
                //Go to the end of the fragment
                while (bufin[i][0]!='=' && ~feof(in[i])) {Fgets(bufin[i],10000,in[i]);}
                //Add the unlinked symbol if there are more LCB coming
                if (l<lastlcomplete)
                    setData(i,pos[i]++,UNLINKED);
            }
        }
        for (i=0;i<nbgenomes;i++)
            if (pos[i]!=getL())
            {printf("Invalid input file: the sequence for %s is incomplete. %d %d\n",names[i],pos[i],getL());abort();}

        //Clear the memory
        for(i=0;i<nbgenomes;i++) {
            fclose(in[i]);
            free(bufin[i]);
        }
        free(in);
        free(pos);
        free(bufin);
        //gsl_vector_int_free(freqs);
        makePolySites();
    }


    Alignment_xmfa::~Alignment_xmfa() {
        gsl_vector_int_free(map);}

    char Alignment_xmfa::convert(char in) {
        switch (in) {
        case 'a':
            return '0';
        case 'A':
            return '0';
        case 't':
            return '1';
        case 'T':
            return '1';
        case 'c':
            return '2';
        case 'C':
            return '2';
        case 'g':
            return '3';
        case 'G':
            return '3';
        default:
            return 'N';
        }
    }

    void Alignment_xmfa::Fgets(char * buf,int l,FILE * f) {
        fgets(buf,l,f);
        while (buf[0]=='#')
            fgets(buf,l,f);
        if (buf[strlen(buf)-1]=='\n' || buf[strlen(buf)-1]=='\r')
            buf[strlen(buf)-1]='\0';
        //if (buf[strlen(buf)-1]=='\r')
        //    buf[strlen(buf)-1]='\0';
    }

    void Alignment_xmfa::extractName(char * buf,char * buf2) {
        if (buf[0]!='>') {buf2[0]='\0';return;}
        int i=1;
        while (buf[i]==' ') i++;
        strcpy(buf2,buf+i);
        if (strstr(buf2,":")!=NULL) (strstr(buf2,":"))[0]='\0';
    }

}
