__author__ = "Raymart Jay E. Canoy"
__date__ = "06 November 2022"

from overlap import *
from k_mer_reads import *

def pick_maximal_overlap_modified(reads, k):
    """
    This function extracts two reads with maximum overlap.
    """
    reada, readb = None, None
    best_olen = 0

    # Dictionary containing the kMers as keys and reads as values
    kMers = k_mer_reads(reads, k)

    for read in reads:
        a_suffix = read[-k:]

        for _, val in enumerate(kMers[a_suffix]):
            if not val == read:
                olen = overlap(read, val, min_length=k)
                if olen > best_olen:
                    reada, readb = read, val
                    best_olen = olen
    
    # returns only the first encountered best olen
    return reada, readb, best_olen