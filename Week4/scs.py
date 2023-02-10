__reference__ = "Coursera's Algorithm for DNA Sequencing"
__date__ = "06 November 2022"

from itertools import permutations
from overlap import *

def scs(ss):
    """
    This function assembles the sequence from the inputted reads
    by finding the shortest common superstring in the reads.
    """

    shortest_sup_list = set()
    shortest_sup = None

    ## Finds the first encountered shortest superstring
    for supers in permutations(ss):         # permutes all the possible reads
        sup = supers[0]                     # starts always at the first element of every permuted reads
        for ind in range(len(supers)-1):
            olen = overlap(supers[ind], supers[ind+1], 1)
            sup += supers[ind+1][olen:]     # merges the reads by eliminating the overlap

        if shortest_sup is None or len(sup) < len(shortest_sup):    # fills in the first encountered shortest sup
            shortest_sup = sup
    
    ## Adds the other superstrings
    for supers in permutations(ss):
        sup = supers[0]
        for ind in range(len(supers)-1):
            olen = overlap(supers[ind], supers[ind+1], 1)
            sup += supers[ind+1][olen:]
        
        if len(sup) == len(shortest_sup):
            shortest_sup_list.add(sup)
    
    return sorted(shortest_sup_list), min([len(scs) for scs in shortest_sup_list])