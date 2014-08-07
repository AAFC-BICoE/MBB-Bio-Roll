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
#include "util.h"

namespace wb {

    /*void Util::mat2file(char * filename,gsl_matrix * mat)
{
ofstream f(filename);
for (int i=0;i<mat->size1;i++) {
for (int j=0;j<mat->size2;j++) f << scientific << gsl_matrix_get(mat,i,j) << " ";
f << "\n";
}
f.close();
}*/

    void Util::mat2file(char * filename,gsl_matrix * mat)
    {
        FILE * f=fopen(filename,"w");
        for (unsigned int i=0;i<mat->size1;i++) {
            for (unsigned int j=0;j<mat->size2;j++) fprintf(f,"%e ",gsl_matrix_get(mat,i,j));
            fprintf(f,"\n");
        }
        fclose(f);
    }

    /*
void Util::mat2file(char * filename,gsl_matrix * mat)
{
FILE * f=fopen(filename,"w");
for (int i=0;i<mat->size1;i++) {
for (int j=0;j<mat->size2;j++) {
if (mat->size2-j>5) {fprintf(f,"%e %e %e %e %e ",gsl_matrix_get(mat,i,j),gsl_matrix_get(mat,i,j+1),gsl_matrix_get(mat,i,j+2),
                                                 gsl_matrix_get(mat,i,j+3),gsl_matrix_get(mat,i,j+4));j+=4;} else
fprintf(f,"%e ",gsl_matrix_get(mat,i,j));}
fprintf(f,"\n");
}
fclose(f);
}*/

    void Util::vec2file(char * filename,gsl_vector * vec)
    {
        FILE * f=fopen(filename,"w");
        vec2file(f,vec);
        fclose(f);
    }

    void Util::vec2file(FILE * f,gsl_vector * vec)
    {
        for (unsigned int i=0;i<vec->size;i++) fprintf(f,"%e\n",gsl_vector_get(vec,i));
    }

    void Util::normalize(gsl_vector * v)
    {
        double sum=0.0;
        for (unsigned int i=0;i<v->size;i++)
            sum+=gsl_vector_get(v,i);
        if (sum==0.0) printf("ERROR IN NORMALIZATION\n");
        for (unsigned int i=0;i<v->size;i++)
            gsl_vector_set(v,i,gsl_vector_get(v,i)/sum);
    }

    void Util::normalize(double * v,int size)
    {
        double sum=0.0;
        for (unsigned int i=0;i<size;i++) sum+=v[i];
        if (sum==0.0) printf("ERROR IN NORMALIZATION2 %d\n",size);
        for (unsigned int i=0;i<size;i++) v[i]/=sum;
    }

    int Util::vecsum_char(gsl_vector_char * vec)
    {
        int sum=0;
        for (unsigned int i=0;i<vec->size;i++) sum+=gsl_vector_char_get(vec,i);
        return sum;
    }


    double Util::lBinoProb (int i,int n, double p)
            /*returns the prob of i successes in n trials with prob of sucess p.*/
    {

        double logsum = 0.0;
        double runningtotal = 1.0;
        int j;

        if (i > (n - i))              /*figure out the n-choose-i part */
        {
            for (j = 2; j <= (n - i); j++)
            {
                runningtotal /= j;
                if (runningtotal < UNDERFLOW)
                {
                    logsum += gsl_sf_log (runningtotal);
                    runningtotal = 1.0;
                }
            }
            for (j = i + 1; j <= n; j++)
            {
                runningtotal *= j;
                if (runningtotal > OVERFLOW)
                {
                    logsum += gsl_sf_log (runningtotal);
                    runningtotal = 1.0;
                }
            }
        }
        else
        {
            for (j = 2; j <= i; j++)
            {
                runningtotal /= j;
                if (runningtotal < UNDERFLOW)
                {
                    logsum += gsl_sf_log (runningtotal);
                    runningtotal = 1.0;
                }
            }
            for (j = n - i + 1; j <= n; j++)
            {
                runningtotal *= j;
                if (runningtotal > OVERFLOW)
                {
                    logsum += gsl_sf_log (runningtotal);
                    runningtotal = 1.0;
                }
            }
        }
        logsum += gsl_sf_log (runningtotal);
        logsum += i * gsl_sf_log (p);
        logsum += (n - i) * gsl_sf_log (1 - p);

        return logsum;
    }


    double Util::lbetapdf(double x,double a,double b)
    {
        double para[2];
        para[0]=a;
        para[1]=b;
        double post[2];
        post[0]=x;
        post[1]=1-x;
        return LDirichletProb(para,post,2);
    }

    double Util::LDirichletProb(double prior[],double post[],int length)
            /*returns the log probability of a vector "post" of length "length",
  given a Dirichlet process with prior "prior". */
    {
        double sumprior = 0.0;
        double logsum;
        int i;

        for (i=0; i<length; i++)
            sumprior += prior[i];

        logsum = mylgamma(sumprior);
        for (i=0; i<length; i++)
            logsum += (prior[i]-1.0)*gsl_sf_log(post[i]) - mylgamma(prior[i]);

        return logsum;
    }


    double Util::mylgamma(double z)
    {
        double a[9] = { 0.9999999999995183, 676.5203681218835,
                        -1259.139216722289, 771.3234287757674, -176.6150291498386,
                        12.50734324009056, -0.1385710331296526, 9.934937113930748e-6,
                        1.659470187408462e-7 };
        double lnsqrt2pi = 0.9189385332046727;
        double result;
        long j;
        double tmp;
        if (z <= 0.)
        {
            fprintf(stderr,"lgamma function failed with wrong input (%lf)\n",z);
            exit(-1);
        }
        result = 0.;
        tmp = z + 7.;
        for (j = 9; j >= 2; --j)
        {
            result += a[j - 1] / tmp;
            tmp -= 1.;
        }
        result += a[0];
        result = gsl_sf_log (result) + lnsqrt2pi - (z + 6.5) + (z - 0.5) * gsl_sf_log (z + 6.5);

        return result;
    }


}
