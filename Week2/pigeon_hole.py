__reference__ = "Coursera's Algorithm for Genomic Sequencing"
__note__ = "Modifications have made to extract the matches using the `Index` class"
__date__ = "25 October 2022"

from Index import *
from boyer_moore import boyer_moore
from preprocessing import BoyerMoore

def approximate_match(t, p, k=8, n=2):
    """
    A function which queries the matches of p in t with n substitutions.
    """
    lp = 24                                     # length of p is assumed to be 24
    segment_length = int(round(lp/(n+1)))       # segment length = lp/(n+1)
    all_matches = set()                         # all matches in the of p in t

    index = Index(t, k)                         # extracting all the indeces

    hit_count = 0
    hit_count_bm = 0
    for i in range(n+1):                        
        start = i*segment_length
        end = min((i+1)*segment_length, len(p))
        matches = index.query(p[start:end])
        hit_count += len(matches)

        ## Check: Boyer-Moore
        p_bm = BoyerMoore(p[start:end], alphabet='ACGT')
        matches_bm = boyer_moore(t, p[start:end])[0]
        hit_count_bm += len(matches_bm)

        for m in matches:
            if m < start or m-start+len(p) > len(t):    # skips when m goes beyond or more than length of t
                continue
        
            mismatches = 0
            for j in range(0, start):
                if not p[j] == t[m-start+j]:
                    mismatches += 1
                    if mismatches > n:
                        break

            for j in range(end, len(p)):
                if not p[j] == t[m-start+j]:
                    mismatches += 1
                    if mismatches > n:
                        break

            if mismatches <= n:
                all_matches.add(m - start)

    if hit_count == hit_count_bm:
        return list(all_matches), hit_count
    else:
        raise Exception("Hit count using class Index does not match with Boyer-Moore's hit count")