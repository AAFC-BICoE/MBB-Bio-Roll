///-----------------------------------------------
// Copyright 2012 Wellcome Trust Sanger Institute
// Written by Jared Simpson (js18@sanger.ac.uk)
// Released under the GPL
//-----------------------------------------------
//
// KmerOverlaps - Overlap computation functions
// seeded by exact kmer matches
//
#ifndef KMER_OVERLAPS_H
#define KMER_OVERLAPS_H

#include "multiple_alignment.h"
#include "BWTIndexSet.h"
#include "SampledSuffixArray.h"

// A pair of sequences and an overlap matching them
struct SequenceOverlapPair
{
    std::string sequence[2];
    bool is_reversed;
    SequenceOverlap overlap;
};
typedef std::vector<SequenceOverlapPair> SequenceOverlapPairVector;

namespace KmerOverlaps
{

// Build a multiple alignment for the query, based on initial exact k-matches 
MultipleAlignment buildMultipleAlignment(const std::string& query, 
                                         size_t k,
                                         int min_overlap,
                                         double min_identity,
                                         int bandwidth,
                                         const BWTIndexSet& indices);

// Retrieve matches to the query sequence
SequenceOverlapPairVector retrieveMatches(const std::string& query, 
                                          size_t k,
                                          int min_overlap,
                                          double min_identity,
                                          int bandwidth,
                                          const BWTIndexSet& indices);
};

#endif
