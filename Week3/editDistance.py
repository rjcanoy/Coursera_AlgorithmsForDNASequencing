__reference__ = "Coursera's Algorithm for DNA Sequencing"
__date__ = '31 October 2022'

def editDistance(a, b):
    """
    Edit distance is the minimum number of edits
    (substitutions, insertions, deletions) needed
    to turn one into the other.

    edist(ax, by) = min
        Case 1: edist(a, b) + delta(x, y),
        Case 2: edist(ax, b) + 1
        Case 3: edist(a, by) + 1
    """

    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)

    delta = 1 if a[-1] != b[-1] else 0
    return(min(
        editDistance(a[-1], b[-1]) + delta,
        editDistance(a[-1], b),
        editDistance(a, b[-1])
    ))