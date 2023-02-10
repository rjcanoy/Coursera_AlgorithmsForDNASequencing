__reference__ = "Coursera's Algorithm for genomic sequencing."
__note__ = "Modifications have been made to count for the number of alignment and char comparison"
__date__ = "25 October 2022"

from preprocessing import *

def naive_exact(t, p):
  """
  This function performs a naive-exact matching algorithm
  """
  n = len(t)
  m = len(p)

  occurrences = []
  comparison = 0
  alignment = 0
  for i in range(n - m + 1):
    mismatched = False
    for j in range(m):
      comparison += 1
      if not t[i+j] == p[j]:
        mismatched = True
        break

    if not mismatched:
      occurrences.append(i)
    alignment += 1
  return occurrences, alignment, comparison