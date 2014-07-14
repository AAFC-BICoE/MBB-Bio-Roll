//-------------------------------------------------------------------------------
// 
// MultipleAlignment - Class for constructing and managing a multiple alignment
// constructed from a set of pairwise overlaps
//
// Copyright (C) 2011 Jared Simpson (jared.simpson@gmail.com)
// 
// Permission is hereby granted, free of charge, to any person obtaining a copy of
// this software and associated documentation files (the "Software"), to deal in
// the Software without restriction, including without limitation the rights to
// use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
// of the Software, and to permit persons to whom the Software is furnished to do
// so, subject to the following conditions:
// 
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
// 
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.
// ------------------------------------------------------------------------------
#include "multiple_alignment.h"
#include <math.h>
#include <iostream>
#include <sstream>
#include <string>
#include <cstdlib>
#include <assert.h>
#include <stdio.h>
#include <limits>
#include <algorithm>

//#define MA_DEBUG 1
//#define MA_DEBUG_CONSENSUS 1

// Initialize static members
const char* MultipleAlignment::m_alphabet = "ACGTN-";

//
// MultipleAlignmentElement
//

//
MultipleAlignmentElement::MultipleAlignmentElement(const std::string& _name, 
                                                   const std::string& _sequence,
                                                   const std::string& _quality,
                                                   size_t leading,
                                                   size_t trailing) : name(_name), 
                                                                      padded_sequence(_sequence),
                                                                      padded_quality(_quality),
                                                                      leading_columns(leading),
                                                                      trailing_columns(trailing)
{

}

//
size_t MultipleAlignmentElement::getNumColumns() const
{
    return leading_columns + padded_sequence.size() + trailing_columns;
}

//
size_t MultipleAlignmentElement::getStartColumn() const
{
    return leading_columns;
}

//
size_t MultipleAlignmentElement::getEndColumn() const
{
    return getNumColumns() - trailing_columns - 1;
}

//
char MultipleAlignmentElement::getColumnSymbol(size_t column_idx) const
{
    assert(column_idx < getNumColumns());
    if(column_idx < leading_columns || column_idx >= leading_columns + padded_sequence.size()) {
        return '\0';
    }
    else {
        assert(column_idx - leading_columns < padded_sequence.size());
        return padded_sequence[column_idx - leading_columns];
    }
}

//
char MultipleAlignmentElement::getColumnQuality(size_t column_idx) const
{
    assert(column_idx < getNumColumns());
    if(padded_quality.empty() || 
       column_idx < leading_columns || 
       column_idx >= leading_columns + padded_quality.size()) {
        return '\0';
    }
    else {
        assert(column_idx - leading_columns < padded_sequence.size());
        return padded_quality[column_idx - leading_columns];
    }
}


//
int MultipleAlignmentElement::getPaddedPositionOfBase(size_t idx) const
{
    size_t unpadded_count = 0;
    for(size_t i = 0; i < padded_sequence.size(); ++i) {
        if(padded_sequence[i] != '-') {
            if(unpadded_count == idx)
                return i;
            else
                unpadded_count += 1;
        }
    }
    std::cerr << "Base index out of bounds: " << idx << "\n";
    assert(false);
    return -1;
}

//
void MultipleAlignmentElement::insertGapBeforeColumn(size_t column_index)
{
    // Check if the column to insert the gap falls within the leading columns
    // If so, just increase the number of leading columns to account for the inserted base.
    // If the column index is one greater than the offset, then we want to 
    // insert a gap before the first base. This is equivalent to just
    // extending the offset.
    if(column_index <= leading_columns + 1) {
        leading_columns += 1;
    }
    else {
        assert(column_index > leading_columns);
        size_t insert_position = column_index - leading_columns;
        if(insert_position < padded_sequence.size()) {
            padded_sequence.insert(insert_position, 1, '-');
            if(!padded_quality.empty())
                padded_quality.insert(insert_position, 1, '-');
        }
        else
            trailing_columns += 1;
    }
}

//
void MultipleAlignmentElement::extendTrailing(size_t n)
{
    trailing_columns += n;
}

//
void MultipleAlignmentElement::trimLeading(size_t n)
{
    assert(n <= leading_columns);
    leading_columns -= n;
}

//
void MultipleAlignmentElement::trimTrailing(size_t n)
{
    assert(n <= trailing_columns);
    trailing_columns -= n;
}

//
std::string MultipleAlignmentElement::getUnpaddedSequence() const
{
    std::string out;
    for(size_t i = 0; i < padded_sequence.size(); ++i) {
        if(padded_sequence[i] != '-')
            out.push_back(padded_sequence[i]);
    }
    return out;
}

//
std::string MultipleAlignmentElement::getPrintableSubstring(size_t start_column, 
                                                            size_t num_columns) const
{
    std::string out;
    size_t i = 0;
    while(i < num_columns) {
        char symbol = getColumnSymbol(start_column + i);
        out.push_back(symbol != '\0' ? symbol : ' ');
        ++i;
    }
    return out;
}

//
// SymbolCount
//

//
bool SymbolCount::lexicographicOrder(const SymbolCount& a, const SymbolCount& b) 
{ 
    return a.symbol < b.symbol; 
}

//
bool SymbolCount::countOrder(const SymbolCount& a, const SymbolCount& b) 
{ 
    return a.count < b.count; 
}

//
bool SymbolCount::countOrderDescending(const SymbolCount& a, const SymbolCount& b) 
{ 
    return a.count > b.count; 
}

//
// MultipleAlignment
//

//
void MultipleAlignment::addBaseSequence(const std::string& name, 
                                        const std::string& sequence, 
                                        const std::string& quality)
{
    m_sequences.push_back(MultipleAlignmentElement(name, sequence, quality, 0, 0));
}

// See header
void MultipleAlignment::addOverlap(const std::string& incoming_name,
                                   const std::string& incoming_sequence,
                                   const std::string& incoming_quality,
                                   const SequenceOverlap& reference_incoming_overlap)
{
    // This function cannot be called before a base element has been added
    assert(!m_sequences.empty());
    MultipleAlignmentElement* template_element = &m_sequences.front();
    _addSequence(incoming_name, incoming_sequence, incoming_quality, template_element, reference_incoming_overlap, false);
}

//
void MultipleAlignment::addExtension(const std::string& incoming_name,
                                     const std::string& incoming_sequence,
                                     const std::string& incoming_quality,
                                     const SequenceOverlap& previous_incoming_overlap)
{
    // This function cannot be called before a base element has been added
    assert(!m_sequences.empty());
    MultipleAlignmentElement* template_element = &m_sequences.back();
    _addSequence(incoming_name, incoming_sequence, incoming_quality, template_element, previous_incoming_overlap, true);
}

// Adds a new string into the multiple alignment using the overlap
// between the incoming sequence and an existing sequence in the
// multiple alignment to calculate the new padded string
void MultipleAlignment::_addSequence(const std::string& name,
                                     const std::string& sequence,
                                     const std::string& quality, 
                                     MultipleAlignmentElement* template_element, 
                                     const SequenceOverlap& overlap,
                                     bool is_extension)
{
    // Get the padded sequence for the template element
    const std::string& template_padded = template_element->padded_sequence;

    // The output padded sequence for the incoming
    std::string padded_output;
    std::string padded_quality;
    
    // Sanity checks
    assert(quality.empty() || quality.size() == sequence.size());

    // Iterate over the cigar string and the padded sequence of the template element
    // to determine where to insert gap symbols
    size_t cigar_index = 0;
    size_t template_index = template_element->getPaddedPositionOfBase(overlap.match[0].start);
    size_t incoming_index = overlap.match[1].start;

    // If extending the multiple alignment, the first
    // base of the incoming sequence must be aligned.
    if(is_extension) 
        assert(incoming_index == 0);
    
    size_t template_leading = template_element->leading_columns;
    size_t incoming_leading = template_index + template_leading;

    // Expand the cigar for easier parsing
    std::string expanded_cigar = expandCigar(overlap.cigar);
    assert(!expanded_cigar.empty());
    assert(template_index < template_padded.size());
    assert(template_padded[template_index] != '-');

#ifdef MA_DEBUG
    std::cout << "Cigar: " << expanded_cigar << "\n";
    std::cout << "template: " << template_padded.substr(template_index) << "\n";
    std::cout << "incoming: " << sequence.substr(incoming_index) << "\n";
    std::cout << "Pairwise:\n";
    overlap.printAlignment(template_element->getUnpaddedSequence(), sequence);
#endif

    while(cigar_index < expanded_cigar.size()) {

        // Check if we are in an existing template gap. This must be handled
        // seperately
        bool in_template_gap = template_padded[template_index] == '-';
        if(in_template_gap) {
            // If we are in a incoming sequence insertion
            // (cigar D) then we are adding a base into a known
            // gap. Add the current incoming base to the output
            if(expanded_cigar[cigar_index] == 'I') {
                padded_output.push_back(sequence[incoming_index]);
                if(!quality.empty())
                    padded_quality.push_back(quality[incoming_index]);

                incoming_index += 1;
                cigar_index += 1;
                template_index += 1;
            } else { 
                // This is an insertion that is in some other sequence
                // in the multiple alignment. Add a gap to the padded output
                padded_output.push_back('-');
                if(!quality.empty())
                    padded_quality.push_back('-');
                
                // Increment the template index
                template_index += 1;    
            }
        } else {
            // Not a template gap
            switch(expanded_cigar[cigar_index]) {
                case 'M':
                    padded_output.push_back(sequence[incoming_index]);
                    if(!quality.empty())
                        padded_quality.push_back(quality[incoming_index]);

                    incoming_index += 1;
                    template_index += 1;
                    cigar_index += 1;
                    break;
                case 'I':
                    insertGapBeforeColumn(template_index + template_leading);
                    padded_output.push_back(sequence[incoming_index]);
                    if(!quality.empty())
                        padded_quality.push_back(quality[incoming_index]);

                    incoming_index += 1;
                    cigar_index += 1;
                    template_index += 1; // skip the newly introduced gap
                    break;
                case 'D':
                    padded_output.push_back('-');
                    if(!quality.empty())
                        padded_quality.push_back('-');
                        
                    cigar_index += 1;
                    template_index += 1;
                    break;
            }
        }
    }

    // Now that the alignment has been built, add the remaining bases of the incoming sequence
    // All other elements of the multiple alignment will be updated to increase the number of
    // trailing columns
    if(is_extension) {
        //printf("Extending the alignment %zu bases\n", sequence.size() - incoming_index);
        padded_output.append(sequence.substr(incoming_index));

        // Ensure that the incoming sequence ends at least as far as the last base
        // currently in the multiple alignment. Otherwise this sequence is a containment
        // and we can not deal with it.
        size_t incoming_columns = padded_output.size() + incoming_leading;
        assert(incoming_columns >= m_sequences.front().getNumColumns());

        // Extend all other sequences to have the same number of columns as the incoming sequence
        for(size_t i = 0; i < m_sequences.size(); ++i)
            m_sequences[i].extendTrailing(sequence.size() - incoming_index);

    }

    // Calculate the number of unfilled columns of the multiple alignment that come after
    // the padded sequence
    size_t incoming_trailing = template_element->getNumColumns() - padded_output.size() - incoming_leading;

    if(is_extension)
        assert(incoming_trailing == 0);

    MultipleAlignmentElement incoming_element(name, padded_output, padded_quality, 
                                              incoming_leading, incoming_trailing);

    m_sequences.push_back(incoming_element);
}

bool MultipleAlignment::isValid() const
{
    size_t total_columns = getNumColumns();
    size_t i = 0;
    while(i < total_columns) {
        if(getPileup(i).empty())
            return false;
        ++i;
    }
    return true;
}

std::string MultipleAlignment::calculateBaseConsensus(int min_call_coverage, int min_trim_coverage)
{
    assert(!m_sequences.empty());
    std::string consensus_sequence;
    MultipleAlignmentElement& base_element = m_sequences.front();
    size_t start_column = base_element.getStartColumn();
    size_t end_column = base_element.getEndColumn();
    
    // This index records the last base in the consensus that had coverage greater than
    // min_trim_coverage. After the consensus calculation the read is trimmed back to this position
    int last_good_base = -1;

    for(size_t c = start_column; c <= end_column; ++c) {
        std::vector<int> counts = getColumnBaseCounts(c);

        char max_symbol = '\0';
        int max_count = -1;
        int total_depth = 0;

#ifdef MA_DEBUG_CONSENSUS
        printf("%zu\t", c);
#endif
        for(size_t a = 0; a < m_alphabet_size; ++a) {
            char symbol = m_alphabet[a];
            total_depth += counts[a];

            if(symbol != 'N' && counts[a] > max_count) {
                max_symbol = symbol;
                max_count = counts[a];
            }
#ifdef MA_DEBUG_CONSENSUS
            printf("%c:%d ", symbol, counts[a]);
#endif
        }

        char base_symbol = base_element.getColumnSymbol(c);
        int base_count = counts[symbol2index(base_symbol)];
        
        // Choose a consensus base for this column. Only change a base
        // if has been seen less than min_call_coverage times and the max
        // base in the column has been seen more times than the base symbol
        char consensus_symbol;
        if(max_count > base_count && base_count < min_call_coverage)
            consensus_symbol = max_symbol;
        else
            consensus_symbol = base_symbol;
        
        // Output a symbol to the consensus. Skip padding symbols and leading
        // bases that are less than the minimum required depth to avoid trimming
        if(consensus_symbol != '-' &&
            (!consensus_sequence.empty() || total_depth >= min_trim_coverage))
                consensus_sequence.push_back(consensus_symbol);

        // Record the position of the last good base
        if(total_depth >= min_trim_coverage) {
            int consensus_index = consensus_sequence.size() - 1;
            if(consensus_index > last_good_base)
                last_good_base = consensus_index;
        }
#ifdef MA_DEBUG_CONSENSUS
        printf("CALL: %c\n", consensus_symbol);
#endif 
    }

    if(last_good_base != -1)
        consensus_sequence.erase(last_good_base + 1);
    else
        consensus_sequence.clear();

    return consensus_sequence;
}

//
void MultipleAlignment::calculateBaseConsensusLikelihood(std::string* consensus_sequence, std::string* consensus_quality)
{
#ifdef MA_DEBUG_CONSENSUS
    print();
#endif
    assert(!m_sequences.empty());

    consensus_sequence->clear();
    consensus_quality->clear();

    // Probability of emitting a gap symbol when there is a true
    // nucleotide in the sequence.
    const double PROBABILITY_GAP = 0.0001;

    MultipleAlignmentElement& base_element = m_sequences.front();
    size_t start_column = base_element.getStartColumn();
    size_t end_column = base_element.getEndColumn();
    
    for(size_t c = start_column; c <= end_column; ++c) {
        std::vector<int> counts = getColumnBaseCounts(c);

        std::vector<double> likelihoods(m_alphabet_size, 0.0f);

#ifdef MA_DEBUG_CONSENSUS
        std::string pileup;
        std::string quality_pileup;
#endif

        // Update likelihoods using every sequence with a base aligned in this column.
        for(size_t i = 0; i < m_sequences.size(); ++i) {
            char b = m_sequences[i].getColumnSymbol(c);
            char q = m_sequences[i].getColumnQuality(c);
            
            if(b == '\0')
                continue; // no base at this position, skip
            assert(q != '\0');

            // Calculate likelihoods.
            double p_error;
            if(b != '-')
                p_error = quality2prob(q);
            else
                p_error = PROBABILITY_GAP;

            // The probabilty the base call is correct.
            double p_match = 1.0f - p_error;
            double lp_match = log(p_match);

            // The true underlying base is different than base call. 
            // We don't have quality scores for all possible calls so we use p_error / 3
            double p_mismatch = p_error / 3;
            double lp_mismatch = log(p_mismatch);

            // Update likelihoods
            for(size_t a = 0; a < m_alphabet_size; ++a) {
                char a_symbol = m_alphabet[a];
                if(a_symbol == b)
                    likelihoods[a] += lp_match;
                else
                    likelihoods[a] += lp_mismatch;
            }

#ifdef MA_DEBUG_CONSENSUS
            pileup.push_back(b);
            quality_pileup.push_back(q);
#endif
        }

        // Calculate most likely symbol
        char call_symbol = 'N';
        double max_likelihood = -std::numeric_limits<double>::max();
        double sum_probability = 0.0f;

        for(size_t a = 0; a < m_alphabet_size; ++a) {
            if(likelihoods[a] > max_likelihood) {
                call_symbol = m_alphabet[a];
                max_likelihood = likelihoods[a];
            }
            sum_probability += exp(likelihoods[a]);
        }

        double p_consensus_error = 1.0f - (exp(max_likelihood) / sum_probability);
        char quality_symbol = prob2quality(p_consensus_error);

#ifdef MA_DEBUG_CONSENSUS
        // Print stats
        printf("Likelihoods:");
        for(size_t a = 0; a < m_alphabet_size; ++a) {
            char a_symbol = m_alphabet[a];
            printf("%c=%.2lf ", a_symbol, likelihoods[a]);
        }
        printf(" Call: %c Perror: %.8lf Qscore: %c Pileup: %s Quality: %s\n", call_symbol, p_consensus_error, quality_symbol, pileup.c_str(), quality_pileup.c_str());
#endif
        // Output a symbol to the consensus. Skip padding symbols and leading
        // bases that are less than the minimum required depth to avoid trimming
        if(call_symbol != '-') {
            consensus_sequence->push_back(call_symbol);
            consensus_quality->push_back(quality_symbol);
        }
    }
}

void MultipleAlignment::filterByMismatchQuality(int max_sum_mismatch)
{

    assert(!m_sequences.empty());
    MultipleAlignmentElement& base_element = m_sequences.front();
    size_t start_column = base_element.getStartColumn();
    size_t end_column = base_element.getEndColumn();

    int GAP_PENALTY = 30;

    // A vector to record the total phred scores of mismatching bases
    std::vector<int> scores(m_sequences.size(), 0);

    for(size_t c = start_column; c <= end_column; ++c) {
        char base_symbol = base_element.getColumnSymbol(c);
        char base_quality = base_element.getColumnQuality(c);

        for(size_t i = 1; i < m_sequences.size(); ++i) {
            char symbol = m_sequences[i].getColumnSymbol(c);
            char quality = m_sequences[i].getColumnQuality(c);

            if(symbol != '\0' && symbol != base_symbol) {
                // This is a mismatch
                if(symbol == '-' || base_symbol == '-')
                    scores[i] += GAP_PENALTY;
                else
                    scores[i] += std::min(int(quality) - 33, int(base_quality) - 33);
            }
        }
    }

    // A vector to record which sequences pass the filter.
    // keep_vector[i] == 1 means that sequence i should be kept.
    std::vector<bool> keep_vector(m_sequences.size(), 1);

//    print(400);
    for(size_t i = 1; i < m_sequences.size(); ++i) {
        if(scores[i] > max_sum_mismatch)
            keep_vector[i] = 0;
    }   

    // Erase elements from the vector
    filterByVector(keep_vector);
}

//
void MultipleAlignment::filterByCount(int min_count)
{
    assert(!m_sequences.empty());
    MultipleAlignmentElement& base_element = m_sequences.front();
    size_t start_column = base_element.getStartColumn();
    size_t end_column = base_element.getEndColumn();

    // A vector to record which sequences pass the filter.
    // keep_vector[i] == 1 means that sequence i should be kept.
    std::vector<bool> keep_vector(m_sequences.size(), 1);

    for(size_t c = start_column; c <= end_column; ++c) {
        std::vector<int> counts = getColumnBaseCounts(c);
        char base_symbol = base_element.getColumnSymbol(c);

        // Check that the base sequence has a call in this column
        // If not, we do not filter here
        if(base_symbol == '\0')
            continue;

        int base_count = counts[symbol2index(base_symbol)];
        int num_above_min = 0;

        for(size_t a = 0; a < m_alphabet_size; ++a) {
            if(counts[a] >= min_count)
                num_above_min += 1;
        }

        if(num_above_min > 1 && base_count >= min_count) {
            //printf("Column %zu is conflicted: %s\n", c, getColumnCountString(c).c_str());
            // This column is conflicted. Update keep_vector.
            for(size_t i = 1; i < m_sequences.size(); ++i) {
                char symbol = m_sequences[i].getColumnSymbol(c);

                // Remove this sequence if it overlaps the conflicted column,
                // if it does not match the base sequence, and its base count is greater
                // than the threshold
                if(symbol != '\0' && symbol != base_symbol && counts[symbol2index(symbol)] >= min_count)
                    keep_vector[i] = 0;
            }
        }
    }

    // Erase elements from the vector
    filterByVector(keep_vector);
}

//
void MultipleAlignment::filterByVector(const std::vector<bool>& keep_vector)
{
    std::vector<MultipleAlignmentElement> filtered_sequences;
    for(size_t i = 0; i < m_sequences.size(); ++i) {
        if(keep_vector[i])
            filtered_sequences.push_back(m_sequences[i]);
    }

    m_sequences.swap(filtered_sequences);
    trimEmptyColumns();
}

std::string MultipleAlignment::getUnpaddedSequence(size_t row) const
{
    assert(row < m_sequences.size());
    return m_sequences[row].getUnpaddedSequence();
    
}

//
char MultipleAlignment::getSymbol(size_t row, size_t col) const
{
    assert(row < m_sequences.size());
    return m_sequences[row].getColumnSymbol(col);
}

//
size_t MultipleAlignment::getNumColumns() const
{
    assert(!m_sequences.empty());
    return m_sequences.front().getNumColumns();
}

//
size_t MultipleAlignment::getNumRows() const
{
    return m_sequences.size();
}

//
std::string MultipleAlignment::getPileup(size_t idx) const
{
    std::string pileup;
    for(size_t i = 0; i < m_sequences.size(); ++i) {
        char symbol = m_sequences[i].getColumnSymbol(idx);
        if(symbol != '\0')
            pileup.push_back(symbol);
    }
    return pileup;
}

// Order the indices of the m_sequences vector by left-coordinate of the alignment on m_sequence[0]
struct SequencePrintOrder
{
    SequencePrintOrder(const std::vector<MultipleAlignmentElement>& sequence) : m_sequences(sequence) {}
    bool operator()(size_t i, size_t j)
    {
        if(i == 0)
            return true;
        if(j == 0)
            return false;
        return m_sequences[i].leading_columns < m_sequences[j].leading_columns;
    }
    private:
        const std::vector<MultipleAlignmentElement>& m_sequences;
};

//
void MultipleAlignment::print(size_t max_columns) const
{
    if(m_sequences.empty())
        return;

    size_t total_columns = m_sequences.front().getNumColumns();

    std::vector<size_t> sequence_index_order(m_sequences.size(), 0);

    // Initialize order
    for(size_t i = 0; i < sequence_index_order.size(); ++i)
        sequence_index_order[i] = i;

    // Sort sequences by the first aligned base on sequence[0]
    SequencePrintOrder sorter(m_sequences);
    std::stable_sort(sequence_index_order.begin(), sequence_index_order.end(), sorter);

    // Make a simple consensus to use as a mask
    std::string consensus = getPaddedConsensus();

    // Print the multiple alignment in segments
    for(size_t c = 0; c < total_columns; c += max_columns) {
        size_t remaining = total_columns - c;
        size_t slice_size = max_columns < remaining ? max_columns : remaining;

        // Print the consensus
        printf("\t%s\tC\n", consensus.substr(c, slice_size).c_str());

        for(size_t i = 0; i < sequence_index_order.size(); ++i) {
            size_t current_index = sequence_index_order[i];

            // Build the output string
            std::string print_string;
            for(size_t j = c; j < slice_size + c; ++j) {
                char consensus_symbol = consensus[j];
                char row_symbol = m_sequences[current_index].getColumnSymbol(j);

                if(row_symbol == '\0')
                    print_string.push_back(' '); // no base for this column
                else if(row_symbol == '-' || row_symbol != consensus_symbol)
                    print_string.push_back(row_symbol); // always show sequence for row 0, gaps and mismatches
                else
                    print_string.push_back('.'); // mask matches
            }
            // Check if this string is blank, if so don't print it
            if(print_string.find_first_not_of(" ") != std::string::npos)
                printf("\t%s\t%s\n", print_string.c_str(), m_sequences[i].name.c_str());
        }
        printf("\n\n");
    }
}

//
void MultipleAlignment::printPileup() const
{
    if(m_sequences.empty())
        return;

    // Get the total number of columns in the alignment
    size_t num_columns = m_sequences.front().getNumColumns();
    size_t num_sequences = m_sequences.size();
    for(size_t i = 0; i < num_columns; ++i) {
        std::string counts_str = getColumnCountString(i);
        std::string pileup;
        std::string quality;
        for(size_t j = 0; j < num_sequences; ++j) {
            // sanity check that the columns are set up correctly
            assert(m_sequences[j].getNumColumns() == num_columns);
            char symbol = m_sequences[j].getColumnSymbol(i);
            if(symbol != '\0')
                pileup.push_back(symbol);

            char quality_symbol =  m_sequences[j].getColumnQuality(i);
            if(quality_symbol != '\0')
                quality.push_back(quality_symbol);

        }
        printf("%zu\t%s\t%s\t%s\n", i, pileup.c_str(), quality.c_str(), counts_str.c_str());
    }
}

//
std::string MultipleAlignment::getPaddedConsensus() const
{
    std::string out;
    for(size_t i = 0; i < getNumColumns(); ++i) {
        SymbolCountVector symbol_counts = getSymbolCountVector(i);
        assert(!symbol_counts.empty());
        std::sort(symbol_counts.begin(), symbol_counts.end(), SymbolCount::countOrderDescending);
        out.append(1, symbol_counts.front().symbol);
    }
    return out;
}

//
void MultipleAlignment::insertGapBeforeColumn(size_t column_index)
{
    for(size_t i = 0; i < m_sequences.size(); ++i) {
        m_sequences[i].insertGapBeforeColumn(column_index);
    }
}

//
void MultipleAlignment::trimEmptyColumns()
{
    size_t num_columns = getNumColumns();
    size_t leading_empty = 0;
    while(getPileup(leading_empty).empty())
        leading_empty += 1;
   
    size_t trailing_empty = 0;
    while(getPileup(num_columns - 1 - trailing_empty).empty())
        trailing_empty += 1;
   
    size_t num_rows = getNumRows();
    for(size_t i = 0; i < num_rows; ++i) {
        m_sequences[i].trimLeading(leading_empty);
        m_sequences[i].trimTrailing(trailing_empty);
    }
}

//
std::string MultipleAlignment::expandCigar(const std::string& cigar)
{
    std::string out;
    std::stringstream parser(cigar);
    int length;
    char symbol;
    while(parser >> length >> symbol)
        out.append(length, symbol);
    return out;
}

//
int MultipleAlignment::symbol2index(char symbol) const
{
    switch(symbol) {
        case 'A':
            return 0;
        case 'C':
            return 1;
        case 'G':
            return 2;
        case 'T':
            return 3;
        case 'N':
            return 4;
        case '-':
            return 5;
    }

    std::cerr << "Error: Unrecognized symbol in multiple alignment\n";
    exit(EXIT_FAILURE);
    return -1;
}

//
double MultipleAlignment::quality2prob(char q) const
{
    assert(q != '\0');
    return pow(10, -(q - 33)/10.0f);
}

//
char MultipleAlignment::prob2quality(double p) const
{
    int phred = 0;
    double lp = log10(p);

    // Clamp very low log probabilities.
    if(lp < -10.0)
        phred = 60;
    else
        phred = (int)(-10 * lp);

    // Clamp score into range
    phred = std::max(0, phred);
    phred = std::min(phred, 60);
    assert(phred >= 0 && phred <= 60);
    return phred + 33;
}

//
std::vector<int> MultipleAlignment::getColumnBaseCounts(size_t idx) const
{
    std::vector<int> out(m_alphabet_size, 0);
    for(size_t i = 0; i < m_sequences.size(); ++i) {
        char symbol = m_sequences[i].getColumnSymbol(idx);
        if(symbol != '\0')
            out[symbol2index(symbol)] += 1;
    }
    return out;
}

//
std::string MultipleAlignment::getColumnCountString(size_t column) const
{
    std::vector<int> counts = getColumnBaseCounts(column);
    std::stringstream out;
    for(size_t i = 0; i < m_alphabet_size; ++i) {
        out << m_alphabet[i] << ":" << counts[i] << " ";
    }
    return out.str();
}

//
SymbolCountVector MultipleAlignment::getSymbolCountVector(size_t column) const
{
    SymbolCountVector out;
    std::vector<int> counts = getColumnBaseCounts(column);
    for(size_t i = 0; i < m_alphabet_size; ++i) {
        if(counts[i] > 0) {
            SymbolCount sc = { m_alphabet[i], counts[i] };
            out.push_back(sc);
        }
    }
    return out;
}

