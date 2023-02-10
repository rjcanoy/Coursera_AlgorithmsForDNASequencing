__reference__ = "Coursera's Algorithm for Genomic Sequencing"
__date__ = "25 October 2022"

import bisect

class SubseqIndex(object):
    """
    Holds a subsequence index for a text T.
    """

    def __init__(self, t, k, ival):
        """
        Create index from all subsequences consisting of k characters
        spaced ival positions apart. E.g., SubseqIndex("ATAT", 2, 2)
        extracts ("AA", 0) and ("TT", 1)
        """

        self.k = k
        self.ival = ival
        self.index = []
        self.span = 1 + ival * (k-1)

        for i in range(len(t) - self.span + 1):
            self.index.append((t[i:i+self.span:ival], i))
        self.index.sort()

    
    def query(self, p):
        """
        Return index hits for first subseq of p.
        """
        subseq = p[:self.span:self.ival]
        i = bisect.bisect_left(self.index, (subseq, -1))
        hits = []

        while i < len(self.index):
            if not self.index[i][0] == subseq:
                break
            hits.append(self.index[i][1])
            i += 1
        
        return hits