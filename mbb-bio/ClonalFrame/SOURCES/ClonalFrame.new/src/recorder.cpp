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
#include "recorder.h"

namespace wb {

    Recorder::Recorder(Param *p,int nbIters,int burnin,int thining)
    {
        this->p=p;
        this->nbIters=nbIters;
        this->burnin=burnin;
        this->thining=thining;
        consensus=new Consensus(p,ceil(1.0*(nbIters-burnin)/thining));
        resultsRecMap=gsl_matrix_calloc(p->a->getN()+p->a->getN()-1,p->a->getL());
        resultsMutMap=gsl_matrix_calloc(p->a->getN()+p->a->getN()-1,p->a->getL());
        resultsAncSeq=gsl_matrix_calloc(p->a->getN()+p->a->getN()-1,p->a->getL());
        resultsPhylo=(char **)calloc(nbIters/thining,sizeof(char *));
        resultsLlhood=gsl_vector_calloc(nbIters/thining);
        resultsNu=gsl_vector_calloc(nbIters/thining);
        resultsMu=gsl_vector_calloc(nbIters/thining);
        resultsRho=gsl_vector_calloc(nbIters/thining);
        resultsDelta=gsl_vector_calloc(nbIters/thining);
    }

    void Recorder::recordBurnin(int it) {
        resultsPhylo[it/thining]=p->tree->newick(p->where,p->tree->nodes,NULL);
        gsl_vector_set(resultsLlhood,it/thining,p->tree->ll+p->tree->llhoodT(p));
        gsl_vector_set(resultsNu,it/thining,p->nu);
        gsl_vector_set(resultsMu,it/thining,p->mu);
        gsl_vector_set(resultsRho,it/thining,p->rho);
        gsl_vector_set(resultsDelta,it/thining,p->delta);
    }

    void Recorder::record(int it) {
        if (p->verbose) {
            int sum=0;
            for (int i=0;i<p->a->getL();i++) sum+=gsl_vector_char_get(p->cf,i);
            printf("mut=%d,rec=%d,mutrec=%d,cf=%d\n",p->mut,p->rec,p->mutrec,p->a->getL()-sum);
            //Count mut,rec,mutrec and cf on branches
            gsl_vector_char * cfvec=gsl_vector_char_calloc(p->a->getL());
            double mut=0.0;double rec=0.0;double mutrec=0.0;double cf=0.0;
            for (int i=0;i<p->a->getN();i++) {p->where[i]->count(p,&mut,&rec,&mutrec,cfvec);
                cf+=p->a->getL();
                for (int j=0;j<p->a->getL();j++) {cf-=gsl_vector_char_get(cfvec,j);gsl_vector_char_set(cfvec,j,0);}
            }
            mut/=p->a->getN();
            rec/=p->a->getN();
            mutrec/=p->a->getN();
            cf/=p->a->getN();
            printf("from isolates to MRCA: mut=%f,rec=%f,mutrec=%f,cf=%f\n",mut,rec,mutrec,cf);
            gsl_vector_char_free(cfvec);
            //Count proportion of intra- and inter-population substitutions
            int mutin=0,mutout=0,recin=0,recout=0;
            p->tree->countInterIntra(p,&mutin,&mutout,&recin,&recout);
            printf("mutin=%d,mutout=%d,recin=%d,recout=%d\n",mutin,mutout,recin,recout);
        }
        recordBurnin(it);
        int nb=(nbIters-burnin)/thining;
        consensus->addTree(p->tree);
        //Record recMap, mutMap and ancSeq for leaves
        for (int i=0;i<p->a->getN();i++)
            for (int j=0;j<p->a->getL();j++) {
            *gsl_matrix_ptr(resultsRecMap,i,j)+=gsl_vector_char_get(p->where[i]->recMap,j)*1.0/nb;
            *gsl_matrix_ptr(resultsAncSeq,i,j)+=gsl_vector_char_get(p->where[i]->ancSeq,j)*1.0/nb;
            if (gsl_vector_char_get(p->where[i]->ancSeq,j)!=gsl_vector_char_get(p->where[i]->father->ancSeq,j)) *gsl_matrix_ptr(resultsMutMap,i,j)+=1.0/nb;
        }
        //Record recMap, mutMap and ancSeq for internal nodes
        for (int i=1;i<p->a->getN()-1;i++)
            for (int j=0;j<p->a->getL();j++) {
            *gsl_matrix_ptr(resultsRecMap,p->a->getN()+i,j)+=gsl_vector_char_get(p->tree->nodes[i]->recMap,j)*1.0/nb;
            *gsl_matrix_ptr(resultsAncSeq,p->a->getN()+i,j)+=gsl_vector_char_get(p->tree->nodes[i]->ancSeq,j)*1.0/nb;
            if (gsl_vector_char_get(p->tree->nodes[i]->ancSeq,j)!=gsl_vector_char_get(p->tree->nodes[i]->father->ancSeq,j)) *gsl_matrix_ptr(resultsMutMap,p->a->getN()+i,j)+=1.0/nb;
        }
    }

    void Recorder::saveResults(char * out,double cutoff) {
        char filename[1000];
        //sprintf(filename,"%srec",out);
        //Util::mat2file(filename,resultsRecMap);
        //sprintf(filename,"%smut",out);
        //Util::mat2file(filename,resultsMutMap);
        //sprintf(filename,"%sseq",out);
        //Util::mat2file(filename,resultsAncSeq);
        sprintf(filename,"%s",out);
        FILE * f=fopen(filename,"w");
        fprintf(f,"#constree\n");
        char * cons=consensus->retConsensus(cutoff);
        fprintf(f,"%s\n",cons);
        free(cons);
        fprintf(f,"#names\n");
        for (int i=0;i<p->a->getN();i++) fprintf(f,"%s\n",p->a->names[i]);
        fprintf(f,"#consevents\n");
        for (int i=0;i<consensus->nbtokeep;i++) {
            HashCell * which=consensus->tokeep[i];
            for (unsigned int j=0;j<p->a->polySites->size;j++)
                if (p->a->getData(0,gsl_vector_int_get(p->a->polySites,j))!=UNLINKED)
                    fprintf(f,"%.2e %.2e ",gsl_vector_get(which->recs,j)/which->nb,gsl_vector_get(which->muts,j)/which->nb);
            fprintf(f,"\n");
        }
        fprintf(f,"#consinfo\n");
        for (int i=0;i<consensus->nbtokeep;i++) {
            HashCell * which=consensus->tokeep[i];
            int k=0;
            if (consensus->sum(which->id)==1) {while (which->id[k]==false) k++;k=k+1;}
            //if (k>0) k=p->a->seqs[k-1];
            fprintf(f,"%d %d %f %f\n",i+1,k,which->age/which->nb,which->ageabove/which->nb);
        }
        /*fprintf(f,"#recpoly\n");
    for (unsigned int i=0;i<resultsRecMap->size1;i++) {
    for (unsigned int j=0;j<p->a->polySites->size;j++)
if (p->a->getData(0,gsl_vector_int_get(p->a->polySites,j))!=UNLINKED)
        fprintf(f,"%e ",gsl_matrix_get(resultsRecMap,i,gsl_vector_int_get(p->a->polySites,j)));
    fprintf(f,"\n");
    }
    fprintf(f,"#mutpoly\n");
    for (unsigned int i=0;i<resultsMutMap->size1;i++) {
    for (unsigned int j=0;j<p->a->polySites->size;j++)
if (p->a->getData(0,gsl_vector_int_get(p->a->polySites,j))!=UNLINKED)
        fprintf(f,"%e ",gsl_matrix_get(resultsMutMap,i,gsl_vector_int_get(p->a->polySites,j)));
    fprintf(f,"\n");
    }*/

        fprintf(f,"#mcmc\n%d\n%d\n%d\n",nbIters,burnin,thining);
        fprintf(f,"%f\n%f\n%f\n%f\n%f\n",p->nubeta1,p->nubeta2,p->thetabase,p->Rbase,p->deltabase);
        fprintf(f,"#phy\n");
        for (unsigned int i=0;i<resultsLlhood->size;i++)
            fprintf(f,"%s\n",resultsPhylo[i]);

        fprintf(f,"#poly\n");
        int minus=0;
        for (unsigned int i=0;i<p->a->polySites->size;i++)
            if (p->a->getData(0,gsl_vector_int_get(p->a->polySites,i))!=UNLINKED)
                fprintf(f,"%d\n",gsl_vector_int_get(p->a->polySites,i)-minus);else minus++;
        //    fprintf(f,"%d\n",gsl_vector_int_get(p->a->map,gsl_vector_int_get(p->a->polySites,i)));

        fprintf(f,"#ll\n");
        Util::vec2file(f,resultsLlhood);

        fprintf(f,"#blocks\n");
        int siz=0;
        for (unsigned int i=0;i<p->a->polySites->size;i++)
            if (p->a->getData(0,gsl_vector_int_get(p->a->polySites,i))!=UNLINKED) siz++;
        else {fprintf(f,"%d\n",siz);siz=0;}
        fprintf(f,"%d\n",siz);

        fprintf(f,"#theta\n");
        for (unsigned int i=0;i<resultsMu->size;i++) gsl_vector_set(resultsMu,i,gsl_vector_get(resultsMu,i)*2.0*p->a->getL());
        Util::vec2file(f,resultsMu);
        for (unsigned int i=0;i<resultsMu->size;i++) gsl_vector_set(resultsMu,i,gsl_vector_get(resultsMu,i)/(2.0*p->a->getL()));

        fprintf(f,"#nu\n");
        Util::vec2file(f,resultsNu);

        fprintf(f,"#delta\n");
        Util::vec2file(f,resultsDelta);

        fprintf(f,"#R\n");
        for (unsigned int i=0;i<resultsRho->size;i++)
            gsl_vector_set(resultsRho,i,gsl_vector_get(resultsRho,i)*2.0*(p->a->getB()*gsl_vector_get(resultsDelta,i)+p->a->getL()-p->a->getB()));
        Util::vec2file(f,resultsRho);
        for (unsigned int i=0;i<resultsRho->size;i++)
            gsl_vector_set(resultsRho,i,gsl_vector_get(resultsRho,i)/2.0/(p->a->getB()*gsl_vector_get(resultsDelta,i)+p->a->getL()-p->a->getB()));

        fprintf(f,"#end\n");
        fclose(f);
    }

    Recorder::~Recorder()
    {
        delete(consensus);
        gsl_matrix_free(resultsRecMap);
        gsl_matrix_free(resultsAncSeq);
        gsl_matrix_free(resultsMutMap);
        gsl_vector_free(resultsLlhood);
        gsl_vector_free(resultsNu);
        gsl_vector_free(resultsMu);
        gsl_vector_free(resultsRho);
        gsl_vector_free(resultsDelta);
        for (int i=0;i<nbIters/thining;i++)
            free(resultsPhylo[i]);
        free(resultsPhylo);
    }

}
