__author__ = 'Raymart Jay E. Canoy'
__date__ = '31 October 2022'

def readGenome(FILENAME):
    """
    This function reads the sequence of a genome in a given filename.
    """

    genome = ''

    with open(FILENAME, 'r') as handle:
        for line in handle:
            if not line[0] == '>':
                genome += line.rstrip()

    return genome