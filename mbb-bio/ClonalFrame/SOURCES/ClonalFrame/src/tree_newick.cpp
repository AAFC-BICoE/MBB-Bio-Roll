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
#include "tree_newick.h"

namespace wb {

    Tree_newick::Tree_newick():Tree() {};

    Tree_newick::Tree_newick(Param * p,Tree *** where,char * name)
        : Tree()
    {
        //Init
        id=0;
        n=p->a->getN();
        (*where)=(Tree **)calloc(n,sizeof(Tree *));
        father=NULL;
        //First read Newick file and create nodes
        ifstream newickFile;
        newickFile.open(name);
        if (!newickFile) {printf("Unable to open input file\n");abort();}
        string newick;
        getline(newickFile,newick);
        newickFile.close();
        //Remove final ';'
        if (newick.at(newick.length()-1)==';') newick=newick.substr(0,newick.length()-1);
        init_newick(&newick,NULL,where,n);
        doAges();

        //Assign seq to leaves
        for (int i=0;i<n;i++) {
            (*where)[i]->ancSeq=gsl_vector_char_calloc(p->a->getL());
            (*where)[i]->recMap=gsl_vector_char_calloc(p->a->getL());
            for (int j=0;j<p->a->getL();j++)
                gsl_vector_char_set((*where)[i]->ancSeq,j,p->a->getData(i,j));
            ungap((*where)[i]->ancSeq,p);
        }

        //Make "nodes" and "n" and ancSeq of internal nodes
        updateNodes();
        for (int j=n-2;j>=0;j--) {
            nodes[j]->ancSeq=gsl_vector_char_calloc(p->a->getL());
            nodes[j]->recMap=gsl_vector_char_calloc(p->a->getL());
            for (int i=0;i<p->a->getL();i++) if (gsl_rng_uniform(p->rng)<
                                                 (nodes[j]->age-nodes[j]->right->age)/(2.0*nodes[j]->age-nodes[j]->right->age-nodes[j]->left->age))
                gsl_vector_char_set(nodes[j]->ancSeq,i,gsl_vector_char_get(nodes[j]->left->ancSeq,i));
            else gsl_vector_char_set(nodes[j]->ancSeq,i,gsl_vector_char_get(nodes[j]->right->ancSeq,i));
        }
    }

    void Tree_newick::init_newick(string* newick,Tree*father,Tree *** where,int N)
    {
        nodes=(Tree **)calloc(N,sizeof(Tree *));
        this->father=father;
        //Find central comma if it exists
        int depth=0;
        int found=0;
        for (unsigned int i=0;i<newick->length();i++)
        {
            if (newick->at(i)=='(')
            {
                depth++;
                continue;
            }
            if (newick->at(i)==')')
            {
                depth--;
                continue;
            }
            if (newick->at(i)==',' && depth==1)
            {
                found=i;
                break;
            }
        }
        //Find last ':' and read dist
        int found2=0;
        depth=0;
        for (unsigned int i=0;i<newick->length();i++)
        {
            if (newick->at(i)=='(')
                depth++;
            if (newick->at(i)==':')
                found2=i;
            if (newick->at(i)==')')
            {
                depth--;
                if (depth==0)
                    found2=0;
            }
        }
        if (found2>0)
        {
            istringstream input(newick->substr(found2+1,newick->length()));
            input >> age;
        }
        else
        {
            age=0.0;
            found2=newick->length();
        }

        if (found==0)
        {
            //Leaf
            left=NULL;
            right=NULL;
            istringstream input(*newick);
            input >> id;
            (*where)[id]=this;
        }
        else
        {
            //Internal node
            id=-1;
            string leftStr =newick->substr(1,found-1);
            string rightStr=newick->substr(found+1,found2-2-found);
            left =new Tree_newick();
            ((Tree_newick*)left )->init_newick(&leftStr ,this,where,N);
            right=new Tree_newick();
            ((Tree_newick*)right)->init_newick(&rightStr,this,where,N);
        }
    }

    void Tree_newick::doAges()
    {
	if (left==NULL) {age=0.0;return;}
	age=left->age;
	((Tree_newick*)left )->doAges();
	((Tree_newick*)right)->doAges();
	age+=left->age;
    }

    Tree_newick::~Tree_newick()
    {
    }


}
