__author__ = 'Raymart Jay E. Canoy'
__date__ = '24 October 2022'

## Initialization
from ctypes import alignment
import get_load_genome as get_load
import preprocessing
from naive_exact import *
from boyer_moore import *
from Index import *
from pigeon_hole import *
from approximate_match_subseq import *

## Loading the excerpt of human chromosome 1
FILENAME = 'chr1.GRCh38.excerpt.fasta'
human_chromosome1 = get_load.load_genome(FILENAME)

## Problem 1
"""
1. How many alignments does the naive matching algoritm try
when matching the string GGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGG
(derived from human Alu sequences to the excerpt of human)
chromosome 1? (Don't consider complements.)
"""
Alu1 = 'GGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGG'
occur_naive, alignment_naive, comparison_naive = naive_exact(human_chromosome1, Alu1)

print(
    """
    \n1. The number of alignments in the naive matching algorithm is %d.
    """ % (alignment_naive)
)

## Problem 2
"""
2. How many character comparison does the naive exact matching algorithm
try when matching the string (derived fom human Alu sequences) to the excerpt
of human chromosome 1? (Don't consider reverse complements.)
"""

print("""
\n2. The number of comparisons in the naive matching algorithm is %d.
""" % (comparison_naive)
)

## Problem 3
"""
3. How many alignment does Boyer-Moore try when matcching the string derived from
human Alu sequences to the excerpt of human chromosome 1?
(Don't consider reverse complements.)
"""
_,_,alignment_bm = boyer_moore(human_chromosome1, Alu1)
print("""
\n3. The number of alignments in the boyer-moore algorithm is %d.
""" % (alignment_bm)
)

## Problem 4
"""
Index-assisted approximate matching
Implement the pigeonhole principle using 'Index' to find matches for partitions.
Assume P always has length 24, and that we are looking for approximate matches with
up to 2 mismatches (substitutions). We will use 8-mer index.
Write a function that, given a length-24 pattern P and given an 'Index' object built
on 8-mers, find all approximate occurrences of P within T with up to 2 mismatches.
Insertions and deletions are not allowed. Don't consider any reverse complements.
How many times does the string GGCGCGGTGGCTCACGCCTGTAAT, which is derived from a human
Alu sequence, occur with up 2 substitutions in the excerpt of human chromosome 1?
(Don't consider reverse complements here.)
"""

p = 'GGCGCGGTGGCTCACGCCTGTAAT'
matches, hit_count = approximate_match(human_chromosome1, p, k=8, n=2)
print("""
\n4. The occurrence of Alu sequence (%s) in the human chromosome 1 is %d.
""" % (p, len(matches))
)

## Problem 5
"""
5. Using the instructions given in Question 4, how many total index hits are
there when searching for occurrences of GGCGCGGTGGCTCACGCCTGTAAT
with up to 2 substitutions in the excerpt of human chromosome 1?
(Don't consider reverse complements/)
"""
print(
    """
    \n5. The total index hits when searching for occurrences of Alu sequence (%s) in the human chromosome 1 is %d.
    """ % (p, hit_count)
)

## Problem 6
"""
6. Write a function that given a length-24 pattern P and given a `SubseqIndex` object built with
k = 8 and ival = 3, finds all approximate occurrences of P within T with up to 2 mismatches.
When using this function, how many total index hits are there when searching
GGCGCGGTGGCTCACGCCTGTAAT with up to 2 substitutions in three excerpt of human chromosome1?
(Again, don't consider reverse complements.)
"""
matches, hit_count = approximate_match_subseq(human_chromosome1, p)
print("""
\n5. The total index hits with up to 2 substitutions in three excerpt is %d
""" % (hit_count))