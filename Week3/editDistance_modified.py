__author__ = 'Raymart Jay E. Canoy'
__date__ = '31 October 2022'

def editDist_modified(x, y):
    """
    This function calculates the modified version of edit distance matrix.
    The first row is set to an offset of [O]. This is done because it the
    location of x in y is not yet known.
    """

    D = []

    for i in range(len(x)+1):
        D.append([0] * (len(y) + 1))
    
    for i in range(len(x)+1):           # the first row is set to an offset of 0.
        D[i][0] = i

    for i in range(1, len(x)+1):        # the rest of the elements are filled using the usual algorithm.
        for j in range(1, len(y)+1):
            distHor = D[i][j-1] + 1
            distVer = D[i-1][j] + 1
            if x[i-1] == y[j-1]:
                distDiag = D[i-1][j-1]
            else:
                distDiag = D[i-1][j-1] + 1
            
            D[i][j] = min(distHor, distVer, distDiag)

    return min(D[-1][:])                # returns the minimum edits required to convert x to y