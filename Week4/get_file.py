__author__ = "Raymart Jay E. Canoy"
__date__ = "06 November 2022"

import requests

def get_file(FILEURL, FILENAME):
    """
    This function gets the sequence file from
    the inputted URL.
    """

    req = requests.get(FILEURL)

    if req.status_code != 200:
        raise Exception('Bad gateway!')

    with open(FILENAME, 'w') as handle:
        handle.write(req.text)

def readGenome(FILENAME):
    """
    This function reads the genome from the
    inputted FILENAME.
    """
    seqs = []
    quals = []

    with open(FILENAME, 'r') as handle:
        while True:
            handle.readline().rstrip()
            seq = handle.readline().rstrip()
            handle.readline().rstrip()
            qual = handle.readline().rstrip()

            if len(seq) == 0:
                break
            else:
                seqs.append(seq)
                quals.append(qual)

    return seqs, quals
    
