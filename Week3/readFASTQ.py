__author__ = "Raymart Jay E. Canoy"
__date__ = '31 October 2022'

def readFASTQ(FILENAME):
    """
    This function extracts the information from a FASTQ file.

    Argument(s):
    filename: FASTQ filename

    Output(s):
    sequences: reads
    qualities: base qualities
    """

    sequences = []
    qualities = []

    with open(FILENAME, 'r') as handle:
        while True:
            handle.readline()
            seq = handle.readline().rstrip()
            handle.readline()
            qual = handle.readline().rstrip()

            if len(seq) == 0:
                break
            else:
                sequences.append(seq)
                qualities.append(qual)
            
    return sequences, qualities
