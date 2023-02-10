__author__ = 'Raymart Jay E. Canoy'
__date__ = '25 October 2022'

from SubseqIndex import *

def approximate_match_subseq(t, p, k=8, ival=3, n=2):
    """
    Finds the occcurrence of p in t using the `SubseqIndex` class.
    """
    index = SubseqIndex(t, k, ival)                 # SubseqIndex class compiles the k-mer (extract from t with ival interval)
    hits = []
    hit_count = 0

    for start in range(3):                          # Looping through ival-1
        hits_initial = index.query(p[start:])
        hit_count += len(hits_initial)

        for hit in hits_initial:
            mismatches = 0

            if start == 0:
                i_int = 1
            else:
                i_int = 0

            for i in range(i_int, len(p)):
                if i % 3 == start:
                    continue
                #print(p[i] == t[hit+i])
                if not p[i] == t[hit+i]:
                    #print(hit, 'start = ', start, 'i = ', i, p[i] == t[hits_initial[0]])
                    mismatches += 1
                    if mismatches > n:
                        break
            

            if mismatches <= n:
                hits.append(hit)

    return hits, hit_count
