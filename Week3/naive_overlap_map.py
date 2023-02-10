__reference__ = "Coursera's Algorithm for DNA Sequencing"
__date__ = "31 October 2022"

from itertools import permutations
from overlap import *

def naive_overlap_map(reads, k):
    """
    Performs the naive overlap map on the reads.
    """

    olaps = {}
    for a, b in permutations(reads, 2):     # Performs a permutation on the reads
        olen = overlap(a, b, min_length=k)
        if olen > 0:                        # If overlap length is greater than zero, append the overlap pairs.
            olaps[(a, b)] = olen
    
    return olaps
