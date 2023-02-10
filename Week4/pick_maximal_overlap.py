__reference__ = "Coursera's Algorithm for DNA sequencing"
__date__ = "06 November 2022"

from itertools import permutations
from overlap import *

def pick_maximal_overlap(reads, k):
    reada, readb = None, None
    best_olen = 0

    for a, b in permutations(reads, 2):
        olen = overlap(a, b, min_length=k)
        if olen > best_olen:
            reada, readb = a, b
            best_olen = olen

    # returns only the first encountered best olen
    return reada, readb, best_olen    