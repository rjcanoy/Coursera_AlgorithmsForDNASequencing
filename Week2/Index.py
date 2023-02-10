_author__ = "Ben Langmead"

import bisect

class Index(object):
    def __init__(self, t, k):
        """
        Create index from all substrings of size 'length'.
        """

        self.k = k
        self.index = []
        for i in range(len(t) - k + 1):
            self.index.append((t[i:i+k], i))
        self.index.sort()
    
    def query(self, p):
        """
        Return index hits for first k-mer of P.
        """

        kmer = p[:self.k]
        i = bisect.bisect_left(self.index, (kmer, -1))
        hits = []

        while i < len(self.index):
            if self.index[i][0] != kmer:
                break
            hits.append(self.index[i][1])
            i += 1
        return hits
