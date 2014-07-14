//-----------------------------------------------
// Copyright 2009 Wellcome Trust Sanger Institute
// Written by Jared Simpson (js18@sanger.ac.uk)
// Released under the GPL
//-----------------------------------------------
//
// TransitiveGroup - A set of edges that form a 
// mutually transitive set wrt a given vertex
//
#ifndef TRANSITIVEGROUPS_H
#define TRANSITIVEGROUPS_H

#include <vector>
#include "MultiOverlap.h"

// Forward declare
class Edge;
class Vertex;
struct EdgeDesc;

typedef std::vector<Edge*> EdgePtrVec;

class TransitiveGroup
{
    public:
        TransitiveGroup(Vertex* pVertex, Edge* pIrreducible);
        
        void add(Edge* pEdge);
        
        Edge* getIrreducible() const;
        Edge* getEdge(size_t idx) const;
        Edge* getEdge(EdgeDesc ed) const;
        MultiOverlap getMultiOverlap() const;
        bool hasEdge(EdgeDesc ed) const;
        size_t numElements() const;

        // IO
        void print() const;
        void printMultiOverlap() const;

    private:

        // data
        Vertex* m_pVertex;
        EdgePtrVec m_edges;
};

#endif
