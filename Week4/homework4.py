__author__ = 'Raymart Jay E. Canoy'
__date__ = '06 November 2022'

## (00) Initialization
from scs import *
from get_file import *
from greedy_scs import *

## (01) Problem 1
"""
It's possible for there to be multiple different
shortest common superstrings for thee same set of
input strings. Consider the input strings ABC, BCA,
CAB. One shortest common superstring is ABCAB but
another iss BCABA and another is CABCA.

What is the length of the shortest common superstring
of the following strings?

CCT, CTT, TGC, TGG, GAT, ATT
"""
ss1 = ['CCT', 'CTT', 'TGC', 'TGG', 'GAT', 'ATT']
shortest_sup_list, shortest_sup_length = scs(ss1)

print(
    """
    1. The length of the shortest common superstring of 
    CCT, CTT, TGC, TGG, GAT, ATT is %d
    """ % (shortest_sup_length)
)

## (02) Problem 2
"""
How many different shortest common superstrings are there
for the input strings given in the previous question?

"""

print(
    """
    2. The number of shortest common superstrings of
    CCT, CTT, TGC, GAT, ATT is %d
    """ % (len(shortest_sup_list))
)

## (03) Problem 3
"""
All the reads are the same length (100 bases) and are exact
copies of substrings from the forward strand of the virus genome.
You don't have to worry about sequencing errors, ploidy of reads coming
from the reverse strand.

Assemble these reads using of the approaches discussed, such as greedy
shortest common superstring. Since there are many reads, you might consider
ways to make the algorithm faster, such as thee one discussed in the programming
assignment in the previous module.

How many As are there in the full, assembled genome?
Hint: The virus genome you are assembling is exactly 15,894 bases long.
"""

FILENAME = 'ads1_week4_reads.fq'
reads, _ = readGenome(FILENAME)

virus_genome = greedy_scs(reads, 10)

# Saving the file
new_filename = 'virus_genome.txt'
with open(new_filename, 'w') as handle:
    handle.write(virus_genome)

# Counting the number of As in the full assembled genome
print(
    """
    3. The number of As in the full, assemble genome is %d.
    """ % len([nuc for nuc in virus_genome if nuc == 'A'])
)

## 4. Problem 4
print(
    """
    4. The number of Ts in the full, assemleb genome is %d.
    """ % len([nuc for nuc in virus_genome if nuc == 'T'])
)