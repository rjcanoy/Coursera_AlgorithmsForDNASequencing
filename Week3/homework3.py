__author__ = "Raymart Jay E. Canoy"
__date__ = "31 October 2022"

## (00) Initialization
from sys import ps2
from readGenome import readGenome
from editDistance_modified import *
from readFASTQ import *
from k_mer_reads import *
from naive_overlap_map_modified import *

FILENAME = 'chr1.GRCh38.excerpt.fasta'
human_genome = readGenome(FILENAME)

## (01) Problem 1
"""
What is the edit distance of the best match between pattern
GCTGATCGATCGTACG and the excerpt of human chromosome 1.
(Don't consider reverse complements)
"""
p1 = 'GCTGATCGATCGTACG'
min_editDist1 = editDist_modified(p1, human_genome)
print(
    """
    1. The  best match between pattern %s and the excerpt of human
    chromosome 1 has the edit distance of %d.
    """ % (p1, min_editDist1)
    )


## (02) Problem 2
"""
What is the edit distance of the best match betweeen pattern GATTTACCAGATTGAG
and the excerpt of human chromosome 1?
(Don't consider reverse complements.) 
"""
p2 = 'GATTTACCAGATTGAG'
min_editDist2 = editDist_modified(p2, human_genome)
print(
    """
    2. The  best match between pattern %s and the excerpt of human
    chromosome 1 has the edit distance of %d.
    """ % (p2, min_editDist2)
    )


## (03) Problem 3
"""
Find all pairs of reads with an exact suffix/prefix match of length at least 30.
Don't overlap a read with itself; if a read has a suffix/prefix match to itself, 
ignore that match. Ignore reverse complements.
"""
FILENAME = 'ERR26641_1.for_asm.fastq'
reads, _ = readFASTQ(FILENAME)

olaps, nodeOutgoingEdge = naive_overlap_map_modified(reads, k=30)
overlap_pairs = list(olaps.keys())
edges = len(set(overlap_pairs))
print(
    """
    3. The edges in the overlap graph is %d
    """ % edges
)

## Problem 4
nodesOutgoingEdge = []
for overlap_pair in overlap_pairs:
    if not overlap_pair[0] in nodesOutgoingEdge:
        nodesOutgoingEdge.append(overlap_pair[0])

print(
    """
    4. Nodes with outgoing edge is %d.
    """ % len(nodeOutgoingEdge)
)

