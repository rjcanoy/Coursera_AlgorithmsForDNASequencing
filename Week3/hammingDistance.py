__reference__ = "Coursera's Algorithms for DNA Sequencing"
__date__ = "31 October 2022"

def hammingDistance(y, x):
    """
    The lengths of X and Y are the same.

    Hamming distance is the minimum number
    of substitutions needed to turn one 
    into the other.
    """

    min_num_sub = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            min_num_sub += 1

    return min_num_sub