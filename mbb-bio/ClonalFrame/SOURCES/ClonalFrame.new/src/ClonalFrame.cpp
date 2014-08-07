/***************************************************************************
 *   Copyright (C) 2011 by Xavier Didelot                                  *
 *   xavier.didelot@gmail.com                                              *
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


#ifdef HAVE_CONFIG_H
#include <config.h>
#endif

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <stdlib.h>
#include <stdio.h>
#include <gsl/gsl_randist.h>
#include <unistd.h>

#include "alignment_structure.h"
#include "alignment_xmfa.h"
#include "genes.h"
#include "param.h"
#include "move_hidden.h"
#include "move_hidden2.h"
#include "move_wb.h"
#include "move_ages.h"
#include "move_gap.h"
#include "move_nu.h"
#include "move_mu.h"
#include "move_delta.h"
#include "move_rho.h"
#include "burst.h"
#include "boot.h"
#include "recorder.h"
//#include <sys/time.h>
#include "timeval.h"
#define GSL_E   (2.7182818284590452353602874713526625 /* e */)

using namespace wb;

/*
\namespace wb
@brief contains all the classes of this project
*/

/**
\mainpage
This is ClonalFrame, an implementation of the methods described in Didelot and Falush (2007).

This program is free software; you can redistribute it and/or modify 
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the 
Free Software Foundation, Inc.,
59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
*/

/** Creates and seeds a new random number generator*/
gsl_rng * makerng() {
    const gsl_rng_type *rng_type;
    long int rng_seed;
    gsl_rng * rng;
    gsl_rng_env_setup();
    rng_type = gsl_rng_default;
    rng_seed = gsl_rng_default_seed;
    rng = gsl_rng_alloc (rng_type);
    unsigned int seed;
    FILE *devrandom;

    if ((devrandom = fopen("/dev/urandom","r")) == NULL) {
        seed = (unsigned long) time(NULL);
        printf("Got seed %u from time()\n",seed);
    } else {
        fread(&seed,sizeof(seed),1,devrandom);
        printf("Got seed %u from /dev/urandom\n",seed);
        fclose(devrandom);
    }

    //seed=0;//This is for debugging purposes only
    gsl_rng_set(rng,seed);
    return rng;
}

static const char * help=
        "\
        Usage: ClonalFrame [OPTIONS] inputfile outputfile\n\
            \n\
            Options:\n\
                -x NUM      Sets the number of iterations after burn-in (default is 50000)\n\
                -y NUM      Sets the number of burn-in iterations (default is 50000)\n\
                -z NUM      Sets the number of iterations between samples (default is 100)\n\
                -e NUM      Sets the number of branch-swapping moves per iterations (default \n\
                            is so that half of the time is spent branch-swapping)\n\
                -m NUM      Sets the initial value of theta to NUM (default is Watterson estimate)\n\
                -d NUM      Sets the initial value of delta to NUM (default is 0.001)\n\
                -n NUM      Sets the initial value of nu to NUM (default is 0.01)\n\
                -r NUM      Sets the initial value of R to NUM (default is initial theta/10)\n\
                -M          Do update the value of theta\n\
                -D          Do not update the value of delta\n\
                -N          Do not update the value of nu\n\
                -R          Do not update the value of R\n\
                -T          Do not update the topology\n\
                -A          Do not update the ages of the nodes\n\
                -G          Remove all gaps\n\
                -H          Remove all gaps at non-polymorphic positions\n\
                -t NUM      Indicate which initial tree to use: 0 for a null tree, 1 for a \n\
                            uniformly chosen coalescent tree and 2 for UPGMA tree (default)\n\
                -w FILE     Use Newick file for initial tree\n\
                -a NUM      Sets the first parameter of the beta prior distribution of nu\n\
                -b NUM      Sets the second parameter of the beta prior distribution of nu\n\
                -U          Use uniform priors for rho, theta and delta\n\
                -B          Run in BURST mode\n\
                -C          Run in UPGMA mode with a site-by-site boostrap procedure\n\
                -c          Run in UPGMA mode with a fragment-by-fragment boostrap procedure\n\
                -S NUM      Sets the seed for the random number generator to NUM\n\
                -E NUM      Sets the rate of exponential growth (default is 0)\n\
                -I          Ignores first block in the alignment\n\
                -L          Clean-up the alignment before running ClonalFrame\n\
                -l          Minimum distance between two reference sites (default is 50)\n\
                -v          Verbose mode\n\
                \n";

int main(int argc, char *argv[]) {
    //Interpretation of the command line
    bool structure=false;//true if input is a structure file
    char * inputname=NULL;//input file
    char * mapfile=NULL;//optional map file if the input is a structure file
    char * outputname=NULL;//output file
    int treeinit=2;//0 for Tree_simple, 1 for Tree_coal and 2 for Tree_UPGMA
    char * nwkname=NULL;
    int c;

    printf("This is ClonalFrame version 1.2\n");
    double theta=100.0;
    double delta=0.001;
    double r=10.0;
    double nu=0.01;
    double nubeta1=1.0;
    double nubeta2=1.0;
    double expgrowth=0.0;
    double thetabase=GSL_E;
    double Rbase=GSL_E;
    double deltabase=GSL_E;
    bool seeded=false;
    unsigned int seed=0;
    bool mufix=true;
    bool deltafix=false;
    bool nufix=false;
    bool rhofix=false;
    bool topofix=false;
    bool agefix=false;
    bool gapfix=false;
    bool gapint=true;
    bool burst=false;
    bool boot=false;
    bool boot2=false;
    bool uniprior=false;
    bool verbose=false;
    bool fastcf=false;
    bool ignorefirstblock=false;
    bool cleanup=false;
    bool watterson=true;
    bool initRho=true;
    int nbit=50000;
    int burn=50000;
    int thin=100;
    int nbswaps=0;
    int mindistrefsites=50;

    if (argc==1) {printf("%s",help);exit(0);}
    //optind=0;
    while ((c = getopt (argc, argv, "E:x:y:z:m:d:n:r:t:w:j:e:S:a:b:f:g:l:sMDNRTAGHhBCcUvFILW")) != -1)
        switch (c)
        {
        case('x'):nbit=atoi(optarg);break;
        case('y'):burn=atoi(optarg);break;
        case('z'):thin=atoi(optarg);break;
        case('m'):theta=atof(optarg);watterson=false;break;
        case('d'):delta=atof(optarg);break;
        case('n'):nu=atof(optarg);break;
        case('r'):r=atof(optarg);initRho=false;break;
        case('M'):mufix=false;break;
        case('D'):deltafix=true;break;
        case('N'):nufix=true;break;
        case('R'):rhofix=true;break;
        case('T'):topofix=true;break;
        case('A'):agefix=true;break;
        case('G'):gapfix=true;break;
        case('H'):gapint=true;break;
        case('j'):mapfile=optarg;break;
        case('s'):structure=true;break;
        case('t'):treeinit=atoi(optarg);break;
        case('w'):nwkname=optarg;break;
        case('h'):printf("%s",help);exit(0);break;
        case('B'):burst=true;break;
        case('C'):boot=true;break;
        case('c'):boot2=true;break;
        case('U'):uniprior=true;break;
        case('v'):verbose=true;break;
        case('e'):nbswaps=atoi(optarg);break;
        case('S'):seeded=true;seed=atoi(optarg);break;
        case('a'):nubeta1=atof(optarg);break;
        case('b'):nubeta2=atof(optarg);break;
        case('f'):thetabase=atof(optarg);break;
        case('g'):Rbase=atof(optarg);break;
        case('i'):deltabase=atof(optarg);break;
        case('E'):expgrowth=atof(optarg);break;
        case('F'):fastcf=true;deltafix=true;break;
        case('I'):ignorefirstblock=true;break;
        case('L'):cleanup=true;break;
        case('l'):mindistrefsites=atoi(optarg);break;
        case '?':
            if (isprint (optopt))
                fprintf (stderr, "Unknown option `-%c'.\n", optopt);
            else
                fprintf (stderr,
                         "Unknown option character `\\x%x'.\n",
                         optopt);
            return 1;
        default:
            abort ();
        }
    nbit=nbit+burn;
    if (argc-optind>2) {printf("Too many non option arguments\n");return 1;}
    if (argc-optind==0) {printf("%s",help);exit(0);}
    if (argc-optind>0) inputname=argv[optind++];
    outputname=(char*)calloc(1000,sizeof(char));
    if (argc-optind>0) sprintf(outputname,"%s",argv[optind++]); else sprintf(outputname,"%s.out",inputname);
    if (argc-optind>0) {mapfile=argv[optind++];structure=true;}

    if (verbose) printf("Create a new random number generator\n");
    gsl_rng * rng;
    if (seeded==false) rng=makerng(); else {rng = gsl_rng_alloc (gsl_rng_default);gsl_rng_set(rng,seed);}

    if (verbose) printf("Load the alignment\n");
    Alignment * a;
    if (structure==false) a=new Alignment_xmfa(inputname,ignorefirstblock,mindistrefsites); else
    {a=new Alignment_structure(inputname,mindistrefsites);if (mapfile!=NULL) ((Alignment_structure*)a)->makeMap(mapfile);}
    if (gapfix==true) a->removeGaps();
    if (gapint==true) a->removeGaps(true);
    if (cleanup==true) {a->cleanUp();a->writeToFile("/tmp/out.xmfa");}
    int poly=0;
    for (int i=0;i<a->getL();i++) {
    	bool eq=true;
    	for (int j=1;j<a->getN();j++)
    	    if (a->getData(j,i)!=a->getData(0,i) && a->getData(j,i)!='N' && a->getData(0,i)!='N' && a->getData(j,i)!=UNLINKED && a->getData(0,i)!=UNLINKED) eq=false;
        if (eq==false) poly=poly+1;
    }
    if (poly==0) poly=1;
    double denom=0.0;
    for (int i=1;i<a->getN();i++) denom+=1.0/i;
    if (watterson) theta=poly/denom;
    if (initRho) r=theta*0.1;
    double mu=theta/(2.0*a->getL());
    double rho=r/(2.0*(a->getB()*delta+a->getL()-a->getB()));
    if (verbose) printf("Create the parameters\n");
    Param * param=new Param(a,rng,treeinit);
    if (nwkname!=NULL) param->loadNewick(nwkname);
    param->init(mu,delta,nu,rho);
    param->uniprior=uniprior;
    param->verbose=verbose;
    param->fastcf=fastcf;
    param->nubeta1=nubeta1;
    param->nubeta2=nubeta2;
    param->thetabase=thetabase;
    param->Rbase=Rbase;
    param->deltabase=deltabase;
    if (expgrowth==0.0) expgrowth=1e-10;
    param->expgrowth=expgrowth;
    int nb=0;

    if (burst==true) {
        printf("Entering BURST mode\n");
        Burst * b=new Burst(a);
        param->recorder=new Recorder(param,1,0,1);
        param->recorder->record(0);
        b->burst(param);
        delete(b);
        param->recorder->saveResults(outputname,0.50);
        delete(param->recorder);
        if (verbose) printf("Free the memory\n");
        return(0);
    }

    if (boot || boot2) {
        printf("Entering BOOTSTRAPING mode\n");
        Boot * b=new Boot(a,boot2);
        param->recorder=new Recorder(param,1,0,1);
        param->recorder->record(0);
        b->boot(param);
        delete(b);
        param->recorder->saveResults(outputname,0.75);
        delete(param->recorder);
        if (verbose) printf("Free the memory\n");
        return(0);
    }

    if (verbose) printf("Create the moves\n");
    Move ** mall=(Move **)calloc(20,sizeof(Move *));
    if (agefix==false) mall[nb++]=new Move_ages(rng);//keeps ll ok
    if (topofix==false) {mall[nb++]=new Move_wb(rng,param);((Move_wb*)mall[nb-1])->setNbswaps(nbswaps);}//requires ll but does not keep it ok
    if (gapfix==false) mall[nb++]=new Move_gap(rng,param);//does not need ll, does not keep it ok
    if (nufix==false) mall[nb++]=new Move_nu(rng,param);//does not need ll, does not keep it ok
    Move_hidden * mh=new Move_hidden(rng,param);mall[nb++]=mh;//recalculates the likelihoods after update
    if (mufix==false) mall[nb++]=new Move_mu(rng,param);//keeps ll ok
    if (rhofix==false) mall[nb++]=new Move_rho(rng,param);//keeps ll ok
    if (deltafix==false) mall[nb++]=new Move_delta(rng,param);//keeps ll ok

    Move_hidden * mh2=new Move_hidden(rng,param);
    mh2->move(param);//initiate ll
    delete(mh2);
    if (verbose) printf("Start running the MCMC\n");
    struct timeval tv;
    gettimeofday(&tv,0);
    unsigned long t=tv.tv_sec;
    param->metropolis(mall,nb,nbit,burn,thin,outputname);
    gettimeofday(&tv,0);
    unsigned long t2=tv.tv_sec;
    printf("Time spent in MH in seconds:%d\n",t2-t);

    if (verbose) printf("Free the memory\n");
    for (int i=0;i<nb;i++) delete(mall[i]);
    free(mall);
    gsl_rng_free(rng);
    free(outputname);

    delete param;
    if (structure==false) delete (Alignment_xmfa *)a;
    else delete (Alignment_structure *)a;
    return EXIT_SUCCESS;
}
