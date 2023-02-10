__reference__ = "Coursera's Algorithm for DNA Sequencing"
__date__ = "06 November 2022"

def de_bruijn_ize(s, k):
    """
    This function breaks a string s into nodes and edges.
    """

    edges = []
    nodes = set()

    for i in range(len(s)-k+1):
        edges.append((s[i:i+k-1], s[i+1:i+k]))
        nodes.add(s[i:i+k-1])
        nodes.add(s[i+1:i+k])

    return nodes, edges