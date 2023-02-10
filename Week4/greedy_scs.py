__author__ = "Raymart Jay E. Canoy"
__date__ = "06 November 2022"

from pick_maximal_overlap_modified import *

def greedy_scs(ss, k):
    """
    This function attempts to calculate the shortest common superstring
    by implementing the greedy algorithm.
    """
    read_a, read_b, olen = pick_maximal_overlap_modified(ss, k)
    
    count = 1
    while olen > 0:
        ss.remove(read_a)
        ss.remove(read_b)
        ss.append(read_a + read_b[olen:])

        read_a, read_b, olen = pick_maximal_overlap_modified(ss, k)
        print('Current processing number is %d ...' % (count))
        count += 1
    
    return [''.join(ss)][0]