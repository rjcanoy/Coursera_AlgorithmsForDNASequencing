__reference__ = "Coursera's Algorithm for DNA Sequencing"
__date__ = "06 November 2022"

def overlap(a, b, min_length=3):
    """
    This function calculates the overlap between a and b.
    Overlap refers to the overlap betwee the suffix of a and prefix of b.
    """

    start = 0
    while True:
        start = a.find(b[:min_length], start)
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1