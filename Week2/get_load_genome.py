__author__ = 'Raymart Jay E. Canoy'
__date__ = "25 October 2022"

import requests

def get_file(FILEURL, FILENAME):
    """
    This function gets the inputted filename from a given URL.
    """
    req = requests.get(FILEURL)

    if req.status_code != 200:
        raise Exception('Bad gateway!')

    with open(FILENAME, 'w') as handle:
        handle.write(req.text)


def load_genome(FILENAME):
    """
    This function loads the genomic sequence from a given filename.
    """

    genome = ''
    
    with open(FILENAME, 'r') as handle:
        for line in handle:
            if not line[0] == '>':
                genome += line.rstrip()     # Remove the whitespaces and new line

    return genome