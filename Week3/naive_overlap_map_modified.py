__author__ = "Raymart Jay E. Canoy"
__date__ = "31 October 2022"

from overlap import *
from k_mer_reads import *

def naive_overlap_map_modified(reads, k=30):
    """
    The function performs a naiver overlap algorithm.
    Steps:
    1. It constructs the dictionary containing the k-mers of each reads as keys
       and the reads as the values.
    2. It only performs the overlap algorithm on the values of the keys that match
       with the k-th suffix of the reads
    3. It returns the overlap pairs.
    """

    olaps = {}                                      # Empty overlap dictionary pairs

    kMers = k_mer_reads(reads, k)                   # k-mers dictionary keys

    for read in reads:                              # Looping through the elements in the reads
        a_suffix = read[-k:]
            
        for _, val in enumerate(kMers[a_suffix]):
            if not val == read:                     # Performs the overlap algorithm on the keys that match the suffix
                olen = overlap(read, val, min_length=k)
                if olen > 0:
                    olaps[(read, val)] = olen                    
    
    return olaps