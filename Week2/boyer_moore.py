__reference__ = "Coursera's Algorithm for DNA Sequencing"
__note__ = "Modifications have been made to count the number of alignment and char comparison"
__date__ = "25 October 2022"

from preprocessing import *

def boyer_moore(t, p, reference='ACGT'):
    """
    This function performs an implementation of the Boyer-Moore algorithm.
    """
    n = len(t)
    m = len(p)

    p_bm = BoyerMoore(p, reference)

    occurrences = []
    alignment = 0
    comparison = 0

    i = 0
    while i < (n - m + 1):
        shift = 1
        mismatched = False
        for j in range(m-1, -1, -1):
            comparison += 1
            if not t[i+j] == p[j]:
                skip_bc = p_bm.bad_character_rule(j, t[i+j])
                skip_gs = p_bm.good_suffix_rule(j)
                shift = max(shift, skip_bc, skip_gs)
                mismatched = True
                break
        
        if not mismatched:
            occurrences.append(i)
            skip_gs = p_bm.match_skip()
            shift = max(shift, skip_gs)
        
        i += shift
        alignment += 1

    return occurrences, alignment, comparison