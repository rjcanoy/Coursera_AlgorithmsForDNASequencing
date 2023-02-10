__author__ = "Raymart Jay E. Canoy"
__date__ = "31 October 2022"

from editDist import *
from globalAlignment import *

## Part 1: Using Edit Distance
x = 'GCGTATGC'
y = 'GCTATAC'

D, editDistance_val = editDist(x, y)

print(
    """
    Edit Distance Table: %s, %s
    """ % (x, y)
    )
print('\n'.join([''.join(['{:7}'.format(item) for item in row]) for row in D]))

## Part 2: Using Global Alignment
x_glob = 'GCGTATGC'
y_glob = 'GCGTATGC'

D_global, editDistance_global = globalAlignment(x_glob, y_glob)
print(
    """
    Global Alignment Table: %s, %s
    """ % (x_glob, y_glob)
)
print('\n'.join([''.join(['{:7}'.format(item) for item in row]) for row in D_global]))

D_glob_v2, _ = globalAlignment(x, y)
print(
    """
    Global Alignment Table: %s, %s
    """ % (x, y)
)

print('\n'.join([''.join(['{:7}'.format(item) for item in row]) for row in D_glob_v2]))
