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
#include "move_hidden.h"

namespace wb
{

    Move_hidden::Move_hidden(gsl_rng * rng,Param * p) : Move(rng)
    {
        calculMode=false;
    }


    Move_hidden::~Move_hidden() {}

    void Move_hidden::move(Param *p)
    {
        if (p->verbose) printf("Move hidden\n");
        Tree ** nodes=p->tree->nodes;
        for (int i=p->a->getN()-2;i>=0;i--)
            //if (p->fastcf) movefast(p,nodes[i]); else
            move1(p,nodes[i]);
        p->tree->llhood(p);//Recalculate the likelihoods
    }

    void Move_hidden::move1(Param *p,Tree * t)
    {
        pprop=0.0;
        msgs=(char *)calloc(p->a->getL(),sizeof(char));
        if (t->father==NULL)
        {
            nbmsgs=3;
            nbstates=5;
            makepbeg(p,t);
            makea(p,t);
            makee(p,t);
            makeMsgsroot(t);
            Tree * t=p->tree;
            if (p->fastcf) {forwardfast(p,t);}
            else
            {
                makeq(p->a->mindistrefsites);
                gsl_matrix * f=forward(p);
                backward(p,f,t);
                gsl_matrix_free(f);
            }
        }
        else
        {
            nbstates=9;
            nbmsgs=6;
            makepbeg(p,t);
            makea(p,t);
            makee(p,t);
            makeMsgs(t);
            if (p->fastcf) {forwardfast(p,t);}
            else
            {
                makeq(p->a->mindistrefsites);
                gsl_matrix * f=forward(p);
                backward(p,f,t);
                gsl_matrix_free(f);
            }
        }
        gsl_matrix_free(a);
        gsl_matrix_free(e);
        gsl_vector_free(pbeg);
        if (!p->fastcf)
        {
            for (int i=0;i<nbstates;i++)
            {
                for (int j=0;j<nbstates;j++)
                    free(q[i][j]);
                free(q[i]);
            }
            free(q);
        }
        free(msgs);
    }

    /*  void Move_hidden::forwardfast(Param *p,Tree *t)
  {
    int prevstate;
    gsl_vector * probas=gsl_vector_calloc(nbstates);
    int L=p->a->getL();
    for (unsigned int i=0;i<L;i++)
    {
      if (msgs[i]==0) setState2(t,p,i,0); else
          if (i!=0 && msgs[i-1]!=0) setState2(t,p,i,prevstate); else
        {
          for (unsigned int j=0;j<nbstates;j++) gsl_vector_set(probas,j,gsl_vector_get(pbeg,j));
          int k=i;
          while (k<L && msgs[k]!=0)
          {
            for (unsigned int j=0;j<nbstates;j++) gsl_vector_set(probas,j,gsl_vector_get(probas,j)*gsl_matrix_get(a,j,j)*gsl_matrix_get(e,j,msgs[k]));
            k++;
          }
          Util::normalize(probas);
          prevstate=setState(t,p,i,probas);
        }
    }
    gsl_vector_free(probas);
  }*/

    void Move_hidden::forwardfast(Param *p,Tree *t)
    {
        int prevstate;
        gsl_vector * probas=gsl_vector_calloc(nbstates);
        int L=p->a->getL();
        for (unsigned int i=0;i<L;i++)
        {
            if (msgs[i]==0) setState2(t,p,i,0); else
                if (i!=0 && msgs[i-1]!=0) setState2(t,p,i,prevstate); else
                {
                int top=0,left=0,right=0;
                for (unsigned int j=0;j<nbstates;j++) gsl_vector_set(probas,j,gsl_vector_get(pbeg,j));
                int k=i;
                while (k<L && msgs[k]!=0)
                {
                    for (unsigned int j=0;j<nbstates;j++) gsl_vector_set(probas,j,gsl_vector_get(probas,j)*gsl_matrix_get(a,j,j)*gsl_matrix_get(e,j,msgs[k]));
                    k++;
                }
                Util::normalize(probas);
                prevstate=setState(t,p,i,probas);
            }
        }
        gsl_vector_free(probas);
    }

    gsl_matrix * Move_hidden::forward(Param *p)
    {
        double sum;
        int site,siteprev;
        gsl_matrix * f=gsl_matrix_calloc(nbstates,p->a->polySites->size+1);
        for (int i=0;i<nbstates;i++)
            gsl_matrix_set(f,i,0,gsl_vector_get(pbeg,i));

        for (unsigned int i=0;i<p->a->polySites->size;i++)
        {
            site=gsl_vector_int_get(p->a->polySites,i);
            if (i==0)
                siteprev=-1;
            else
                siteprev=gsl_vector_int_get(p->a->polySites,i-1);
            for (int state=0;state<nbstates;state++)
            {
                sum=0.0;
                for (int j=0;j<nbstates;j++)
                    sum+=gsl_matrix_get(f,j,i)*q[j][state][site-siteprev-1];
                gsl_matrix_set(f,state,i+1,sum*gsl_matrix_get(e,state,msgs[site]));
            }
            Util::normalize(&(gsl_matrix_column(f,i+1).vector));
        }
        return f;
    }

    void Move_hidden::backward(Param * p,gsl_matrix * f,Tree * t)
    {
        //First set the state for all the polymorphic sites
        int L=p->a->getL();
        int *states=(int*)calloc(L,sizeof(int));
        int nbpoly=p->a->polySites->size;
        gsl_vector * probas=gsl_vector_calloc(nbstates);
        for (int j=0;j<nbstates;j++)
            gsl_vector_set(probas,j,gsl_matrix_get(f,j,nbpoly));
        states[gsl_vector_int_get(p->a->polySites,nbpoly-1)]=setState(t,p,L-1,probas);
        for (int i=nbpoly-2;i>=0;i--)
        {
            int polyi =gsl_vector_int_get(p->a->polySites,i);
            int polyi1=gsl_vector_int_get(p->a->polySites,i+1);
            for (int j=0;j<nbstates;j++)
                gsl_vector_set(probas,j,gsl_matrix_get(f,j,i+1)*q[j][states[polyi1]][polyi1-polyi-1]);
            Util::normalize(probas);
            states[gsl_vector_int_get(p->a->polySites,i)]=setState(t,p,polyi,probas);
        }
        gsl_vector_free(probas);

        //Then fill the gaps between polymorphic sites
        int old=p->a->polySites->size-1;
        for (int i=L-2;i>=0;i--)
            if (old==0 || gsl_vector_int_get(p->a->polySites,old-1)!=i)
            {
            int x=states[gsl_vector_int_get(p->a->polySites,old)];
            int y=states[gsl_vector_int_get(p->a->polySites,old-1)];
            int d=gsl_vector_int_get(p->a->polySites,old)- gsl_vector_int_get(p->a->polySites,old-1);
            if (x==y)
                setState2(t,p,i,x);
            if (x!=y && i-1==gsl_vector_int_get(p->a->polySites,old-1))
            {
                fillgap(t,p,gsl_vector_int_get(p->a->polySites,old-1),gsl_vector_int_get(p->a->polySites,old),y,x);
            }
        }
        else
            old--;
        free(states);
    }

    void Move_hidden::fillgap(Tree *t,Param *p,int a,int b,int x,int y)
    {
        //printf("%d %d %d %d\n",a,b,x,y);
        gsl_vector * probas=gsl_vector_calloc(b-a);
        for (int i=0;i<b-a;i++)
            gsl_vector_set(probas,i,gsl_pow_int(gsl_matrix_get(e,x,1),i)*gsl_pow_int(gsl_matrix_get(e,y,1),b-a-i-1)*gsl_pow_int(gsl_matrix_get(this->a,x,x),i)*gsl_pow_int(gsl_matrix_get(this->a,y,y),b-a-i-1)*gsl_matrix_get(this->a,x,y));
        int k=0;
        while (gsl_vector_get(probas,k)==0.0) k++;
        double fact=1.0/gsl_vector_get(probas,k);
        Util::normalize(probas);
        fact*=gsl_vector_get(probas,k);
        double r=gsl_rng_uniform(this->rng);
        int d=0;
        while (r>gsl_vector_get(probas,d))
            r-=gsl_vector_get(probas,d++);
        if (gsl_vector_get(probas,d)==0.0 || fact==0.0 || q[x][y][b-a-1]==0.0) printf("error 1: %e %e %e\n",gsl_vector_get(probas,d),fact,q[x][y][b-a-1]);
        pprop+=gsl_sf_log(gsl_vector_get(probas,d)/fact/q[x][y][b-a-1]);
        for (int i=a+1;i<b;i++)
            if (i-a<=d)
                setState2(t,p,i,x);
        else
            setState2(t,p,i,y);
        gsl_vector_free(probas);
    }

    int Move_hidden::setState(Tree * t,Param * p,int site,gsl_vector * probas)
    {
        int j=0;
        double r;
        if (calculMode==true && gsl_vector_char_get(t->recMap,site)!=9 && gsl_vector_char_get(t->left->recMap,site)!=9)
        {
            j=gsl_vector_char_get(t->left->recMap,site)*2+gsl_vector_char_get(t->right->recMap,site)+1;
            //if (nbstates==9)
            j+=gsl_vector_char_get(t->recMap,site)*4;
            if (nbstates!=9 && gsl_vector_char_get(t->recMap,site)!=0)
                printf("ERROR HERE\n");
        }
        else
        {
            r=0.0;while (r==0.0) r=gsl_rng_uniform(rng);
            while (r>gsl_vector_get(probas,j))
            {
                r-=gsl_vector_get(probas,j);
                j++;
            }
        }
        if (gsl_vector_get(probas,j)==0.0)
            printf("error here r=%f calcMode=%d site=%d j=%d msg=%d recmapabove=%d recmapleft=%d recmapright=%d recmapfather=%d ancseq=%d ancseqleft=%d ancseqfather=%d\n",
                   r,calculMode,site,j,msgs[site],
                   gsl_vector_char_get(t->recMap,site),
                   gsl_vector_char_get(t->left->recMap,site),
                   gsl_vector_char_get(t->right->recMap,site),
                   gsl_vector_char_get(t->father->recMap,site),
                   gsl_vector_char_get(t->ancSeq,site),
                   gsl_vector_char_get(t->left->ancSeq,site),
                   gsl_vector_char_get(t->father->ancSeq,site));
        pprop+=gsl_sf_log(gsl_vector_get(probas,j));
        setState2(t,p,site,j);
        return j;
    }

    void Move_hidden::setState2(Tree *t,Param *p,int site,int j)
    {
        if (calculMode==false)
        {
            if (j==0)
            {
                gsl_vector_char_set(t->left->recMap,site,UNLINKED);
                gsl_vector_char_set(t->right->recMap,site,UNLINKED);
                if (nbstates==9)
                {
                    gsl_vector_char_set(t->recMap,site,UNLINKED);
                }
                gsl_vector_char_set(t->ancSeq,site,UNLINKED);
                //}
            }
            else
            {
                gsl_vector_char_set(t->left->recMap,site,((j-1)>>1)%2);
                gsl_vector_char_set(t->right->recMap,site,(j-1)%2);
                if (nbstates==9)
                {
                    gsl_vector_char_set(t->recMap,site,(j-1)>>2);
                }
            }
            gsl_vector_char_set(t->ancSeq,site,drawSeq(p,t,site));
            //}
        }
        else
        {drawSeq(p,t,site);}
    }

    void Move_hidden::makepbeg(Param * p,Tree *t)
    {
        pbeg=gsl_vector_calloc(nbstates);
        gsl_vector_set(pbeg,0,0.01);
        double dage=0.0;
        int kmax;
        if (nbstates==9)
            kmax=2;
        else
            kmax=1;
        for (int i=0;i<nbstates-1;i++)
        {
            double val=1.0;
            for (int k=0;k<=kmax;k++)
            {
                if (k==0)
                    dage=t->age-t->right->age;
                if (k==1)
                    dage=t->age-t->left ->age;
                if (k==2)
                    dage=t->father->age-t->age;
                if ((i>>k)%2==0)
                    val*=p->delta;
                else
                    val*=p->rho*dage;
                val/=(p->delta+p->rho*dage);
            }
            gsl_vector_set(pbeg,i+1,val);
        }
        Util::normalize(pbeg);
    }

    void Move_hidden::makea(Param * p,Tree * t)
    {
        double dage=0.0;
        int kmax;
        if (nbstates==9)
            kmax=2;
        else
            kmax=1;
        a=gsl_matrix_calloc(nbstates,nbstates);
        for (int i=0;i<nbstates;i++)
            gsl_matrix_set(a,0,i,gsl_vector_get(pbeg,i));
        for (int i=0;i<nbstates-1;i++)
            gsl_matrix_set(a,i+1,0,1.0e-10);
        for (int i=0;i<nbstates-1;i++)
            for (int j=0;j<nbstates-1;j++)
            {
            double val=1.0;
            for (int k=0;k<=kmax;k++)
            {
                if (k==0)
                    dage=t->age-t->right->age;
                if (k==1)
                    dage=t->age-t->left ->age;
                if (k==2)
                    dage=t->father->age-t->age;
                if ((i>>k)%2==0 && (j>>k)%2==0)
                    val*=1.0-p->rho*dage;
                if ((i>>k)%2==1 && (j>>k)%2==1)
                    val*=1.0-p->delta;
                if ((i>>k)%2==0 && (j>>k)%2==1)
                    val*=p->rho*dage;
                if ((i>>k)%2==1 && (j>>k)%2==0)
                    val*=p->delta;
            }
            gsl_matrix_set(a,i+1,j+1,val);
        }
        for (int i=0;i<nbstates;i++)
        {
            double sum=0.0;
            for (int j=0;j<nbstates;j++)
                sum+=gsl_matrix_get(a,i,j);
            for (int j=0;j<nbstates;j++)
                gsl_matrix_set(a,i,j,gsl_matrix_get(a,i,j)/sum);
        }
    }

    void Move_hidden::makee(Param * p,Tree * t)
    {
        double a,m1,m2,m3;
        e=gsl_matrix_calloc(nbstates,nbmsgs);
        gsl_matrix_set(e,0,0,1.0);
        for (int i=0;i<nbstates-1;i++)
        {//nbstates-1
            if (nbstates==9)
                m1=p->mu*(t->father->age-t->age);
            //else
            //    m1=0.5;
            m2=p->mu*(t->age-t->left ->age);
            m3=p->mu*(t->age-t->right->age);
            if (nbstates==9 && (i>>2)%2==1)
                m1=p->nu;
            if ((i>>1)%2==1)
                m2=p->nu;
            if ((i>>0)%2==1)
                m3=p->nu;

            if (nbstates==9)
            {
                gsl_matrix_set(e,i+1,1,(1.0-m1)*(1.0-m2)*(1.0-m3));
                gsl_matrix_set(e,i+1,2,(1.0-m1)*(1.0-m2)*(    m3));
                gsl_matrix_set(e,i+1,3,(    m1)*(1.0-m2)*(1.0-m3));
                gsl_matrix_set(e,i+1,4,(1.0-m1)*(    m2)*(1.0-m3));
                a=0;
                a+=(1.0-m1)*(    m2)*(    m3);
                a+=(    m1)*(1.0-m2)*(    m3);
                a+=(    m1)*(    m2)*(1.0-m3);
                gsl_matrix_set(e,i+1,nbmsgs-1,a);
            }
            else
            {
                gsl_matrix_set(e,i+1,1,(1.0-m2)*(1.0-m3));
                gsl_matrix_set(e,i+1,2,(1.0-m2)*m3+(1.0-m3)*m2);
            }

            Util::normalize(&(gsl_matrix_row(e,i+1).vector));
        }
    }

    void Move_hidden::makeq(int maxDist)
    {
        //Calculate maxDist, the maximum distance between two polymorphic sites and allocate the matrix q
        //int maxDist=mindistrefsites;
        //for (int i=0;i<p->a->polySites->size-1;i++)
        //    maxDist=GSL_MAX(maxDist,
        //                    gsl_vector_int_get(p->a->polySites,i+1)-gsl_vector_int_get(p->a->polySites,i));
        q=(double ***)calloc(nbstates,sizeof(double **));
        for (int i=0;i<nbstates;i++)
        {
            q[i]=(double **)calloc(nbstates,sizeof(double *));
            for (int j=0;j<nbstates;j++)
                q[i][j]=(double *)calloc(maxDist,sizeof(double));
        }

        //Calculate the values in q
        for (int i=0;i<nbstates;i++)
            for (int j=0;j<nbstates;j++)
                q[i][j][0]=gsl_matrix_get(a,i,j);
        for (int l=1;l<maxDist;l++)
        {
            for (int i=0;i<nbstates;i++)
            {
                for (int j=0;j<nbstates;j++)
                {
                    for (int k=1;k<nbstates;k++)
                        q[i][j][l]+=q[i][k][l-1]*gsl_matrix_get(a,k,j)*gsl_matrix_get(e,k,1);
                }
            }
            //sum=0.0;
            //for (int i=0;i<nbstates;i++) for (int j=0;j<nbstates;j++) sum+=q[i][j][l];
            //for (int i=0;i<nbstates;i++) for (int j=0;j<nbstates;j++) q[i][j][l]/=sum;
        }
    }

    char Move_hidden::drawSeq(Param * p,Tree * t,int i)
    {
        if (t->father!=NULL && gsl_vector_char_get(t->left->ancSeq,i)==gsl_vector_char_get(t->right->ancSeq,i) && gsl_vector_char_get(t->left->ancSeq,i)==gsl_vector_char_get(t->father->ancSeq,i))
            return gsl_vector_char_get(t->father->ancSeq,i);
        if (t->father==NULL && gsl_vector_char_get(t->left->ancSeq,i)==gsl_vector_char_get(t->right->ancSeq,i))
            return gsl_vector_char_get(t->left->ancSeq,i);
        double probas[4];
        double mut;
        double sum=0.0;
        for (int k=0;k<4;k++)
        {
            probas[k]=1.0;
            //Proba that father gave k
            if (t->father!=NULL)
            {
                if (gsl_vector_char_get(t->recMap,i)==0)
                    mut=p->mu*(t->father->age-t->age);
                else
                    mut=p->nu;
                if (k+'0'==gsl_vector_char_get(t->father->ancSeq,i))
                    probas[k]*=1.0-mut;
                else
                    probas[k]*=mut/3.0;
            }
            //Proba that k gave left
            if (gsl_vector_char_get(t->left ->recMap,i)==0)
                mut=p->mu*(t->age-t->left ->age);
            else
                mut=p->nu;
            if (k+'0'==gsl_vector_char_get(t->left ->ancSeq,i))
                probas[k]*=1.0-mut;
            else
                probas[k]*=mut/3.0;
            //Proba that k gave right
            if (gsl_vector_char_get(t->right->recMap,i)==0)
                mut=p->mu*(t->age-t->right->age);
            else
                mut=p->nu;
            if (k+'0'==gsl_vector_char_get(t->right->ancSeq,i))
                probas[k]*=1.0-mut;
            else
                probas[k]*=mut/3.0;
            sum+=probas[k];
        }
        for (int k=0;k<4;k++)
            probas[k]/=sum;
        int j=0;
        if (calculMode==true)
            j=gsl_vector_char_get(t->ancSeq,i)-'0';
        else
        {
            double r=gsl_rng_uniform(rng);
            while (r>probas[j])
            {
                r-=probas[j];
                j++;
            }
        }
        if (j>=4 || probas[j]==0) printf("error3\n");
        pprop+=gsl_sf_log(probas[j]);
        return j+'0';
    }

    void Move_hidden::makeMsgs (Tree *t)
    {
        for (unsigned int i=0;i<t->ancSeq->size;i++)
        {
            if (gsl_vector_char_get(t->ancSeq,i)==UNLINKED)
            {
                msgs[i]=0;
                continue;
            }
            if (gsl_vector_char_get(t->father->ancSeq,i)==gsl_vector_char_get(t->left->ancSeq,i) &&
                gsl_vector_char_get(t->father->ancSeq,i)==gsl_vector_char_get(t->right->ancSeq,i))
            {
                msgs[i]=1;
                continue;
            }
            if (gsl_vector_char_get(t->father->ancSeq,i)==gsl_vector_char_get(t->left->ancSeq,i) &&
                gsl_vector_char_get(t->father->ancSeq,i)!=gsl_vector_char_get(t->right->ancSeq,i))
            {
                msgs[i]=2;
                continue;
            }
            if (gsl_vector_char_get(t->father->ancSeq,i)!=gsl_vector_char_get(t->left->ancSeq,i) &&
                gsl_vector_char_get(t->left  ->ancSeq,i)==gsl_vector_char_get(t->right->ancSeq,i))
            {
                msgs[i]=3;
                continue;
            }
            if (gsl_vector_char_get(t->father->ancSeq,i)==gsl_vector_char_get(t->right->ancSeq,i) && gsl_vector_char_get(t->father->ancSeq,i)!=gsl_vector_char_get(t->left ->ancSeq,i))
            {
                msgs[i]=4;
                continue;
            }
            msgs[i]=5;
        }
    }

    void Move_hidden::makeMsgsroot(Tree * t)
    {
        for (unsigned int i=0;i<t->ancSeq->size;i++)
        {
            if (gsl_vector_char_get(t->ancSeq,i)==UNLINKED)
            {
                msgs[i]=0;
                continue;
            }
            if (gsl_vector_char_get(t->left->ancSeq,i)==gsl_vector_char_get(t->right->ancSeq,i))
            {
                msgs[i]=1;
                continue;
            }
            msgs[i]=2;
        }
    }

}
