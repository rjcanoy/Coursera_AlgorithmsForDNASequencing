__author__ = "Raymart Jay E. Canoy"
__date__ = "31 October 2022"

from Index import *

def k_mer_reads(reads, k):
    """
    This function splits each read into
    its k-mers and uses the k-mers as keys
    and the reads as values.
    """

    k_mers = {}

    ## First Element
    read = reads[0]
    index = Index(read, k)
    for ind in index.index:
        k_mers[ind[0]] = [read]

    ## Succeeding Elements
    for i in range(1, len(reads)):
        read = reads[i]
        index = Index(read, k)

        for ind in index.index:
            if not ind[0] in k_mers:
                k_mers[ind[0]] = [read]
            else:
                k_mers[ind[0]].append(read)
    
    return k_mers