import requests

def get_file(FILEURL, FILENAME):
    """
    This function copies the sequencce from
    the inputted URL in the FILENAME.
    """
    req = requests.get(FILEURL)

    if req.status_code != 200:
        raise Exception('Bad gateway.')
    
    with open(FILENAME, 'w') as handle:
        handle.write(req.text)