# -*- coding: utf-8 -*-
__author__ = "Raymart Jay E. Canoy"
__date__ = "25 October 2022"

"""Week2_LectureNotes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N_1BAsN0wXRIt8u5meK1ZzPVbIShWCIV

# Author: Raymart Jay E. Canoy
# Date: 16 October 2022
___

* **Outline**
  1. **Boyer-Moore Algorithm**: An alternative to naive algorithm
  2. **Indexing**: Working on genomes and read-alignment problem
  3. **Pigeon-hole Principle**: On exact and approximare matching problems

### (1) Boyer-Moore basics

* Learn from character comparisons to skip pointless alignments
* Try alignments in left-to-right order, and try character comparisons in right-to-left order
* **Bad character rule:**
  Upon mismatch, skip alignments until
  (a) mismatch becomes a match, or
  (b) P moves past mismatched character
* **Good suffix rule:**
  Let $t=$ substring matched by inner loop; skip until
  (a) there are no mismatches between $P$ and $t$ or
  (b) $P$ moves past $t$

#### Diversion: Repetitive elements

* Transposable elements: Infiltrates the genome
* 45% in the human genome came from transposable elements
  * For example, `Alu` (11%)
  * Read: Cordaux R, Batzer MA. The impact of retrotransposons on human genome evolution. Nat Rev Genet. 2009 Oct; 10(10):691-703
* **Relevance of transposable elements**
  * Transposable elements create ambiguity in the human genome
  * Repettive sequence in the genome are gonna create problem in our problem.
"""

## Pre-processing of strings
import string

def z_array(s):
  """
  Use Z algorithm (Gusfield theorem 1.4.1) to preprocess s
  """
  z = [len(s)] + [0] * (len(s)-1)

  # Initial comparison of s[1:] with prefix
  for i in range(1, len(s)):
    if s[i] == s[i-1]:              # compares the nucleotide in the previos index matches with the current nucleotide
      z[1] += 1                     # if yes, add 1 to the the z list at index 1
    else:                           # otherwise, break
      break

  r, l = 0, 0
  if z[1] > 0:
    r, l = z[1], 1
  
  for k in range(2, len(s)):        # start at index i = 2
    assert z[k] == 0                # assert that the value of z at index i is zero
    if k > r:                       # Case 1: k > r
      # Case 1
      for i in range(k, len(s)):    
        if s[i] == s[i-k]:          # compares the current element with the previous elements
          z[k] += 1
        else:
          break
      r, l = k + z[k] - 1, k
    else:
      # Case 2                      # Case 2: k < r
      # Calculate length of beta
      nbeta = r - k + 1             # nbeta = r - k + 1
      zkp = z[k-l]
      if nbeta > zkp:
        # Case 2a: Zkp wins
        z[k] = zkp
      else:
        # Case 2b: Compare characters just past r
        nmatch = 0
        for i in range(r+l, len(s)):
          if s[i] == s[i-k]:
            nmatach += 1
          else:
            break
        l, r = k, r + nmatch
        z[k] = r - k + 1
  
  return z


def n_array(s):
  """
  Compare the N array (Gusfield theorem 2.2.2) from the Z array
  """
  return z_array(s[::-1])[::-1]

def big_l_prime_array(p, n):
  """
  Compile L' array (Gusfield theorm 2.2.2) using p and N array.
  L'[i] = largest index j less than n such that N[j] = |P[i:]|
  """
  lp = [0] * len(p)
  for j in range(len(p)-1):
    i = len(p) - n[j]
    if i < len(p):
      lp[i] = j + 1

  return lp

def big_l_array(p, lp):
  """
  Compile L array (Gusfield theorem 2.2.2) using p and L' array.
  L[i] = largest index j less than n such that N[j] >= |P[i:]|
  """
  l = [0] * len(p)
  l[1] = lp[1]
  for i in range(2, len(p)):
    l[i] = max(l[i-1], lp[i])
  
  return l

def small_l_prime_array(n):
  """
  Compile lp' array (Gusfield theorem 2.2.4) using N array.
  """
  small_lp = [0] * len(n)
  for i in range(len(n)):
    if n[i] == i+1:                 # prefix matching a suffix
      small_lp[len(n)-i-1] = i+1
  for i in range(len(n)-2, -1, -1): # "smear" them out to the left
    if small_lp[i] == 0:
      small_lp[i] = small_lp[i+1]
  
  return small_lp

def good_suffix_table(p):
  """
  Return tables needed to apply good suffix rule.
  """
  n = n_array(p)
  lp = big_l_prime_array(p, n)
  return lp, big_l_array(p, lp), small_l_prime_array(n)

def good_suffix_mismatch(i, big_l_prime, small_l_prime):
  """
  Given a mismatch at offset i, and given L/L' and l' arrays,
  return amount to shift as determined by good suffix rule.
  """
  length = len(big_l_prime)
  assert i < length
  if i == length - 1:
    return 0
  i += 1      # i points to leftmost matchig position of p
  if big_l_prime[i] > 0:
    return length - big_l_prime[i]
  return length - small_l_prime[i]

def good_suffix_match(small_l_prime):
  """
  Given a full match of P to T, return amount to shift as
  determined by good suffix rule.
  """
  return len(small_l_prime) - small_l_prime[1]

def dense_bad_char_tab(p, amap):
  """
  Given pattern string and list with ordered alphabet characters, create
  and return a dense bad character table. Table is indexed by offset
  then by character.
  """
  tab = []
  nxt = [0] * len(amap)
  for i in range(0, len(p)):
    c = p[i]
    assert c in amap
    tab.append(nxt[:])
    nxt[amap[c]] = i + 1
  return tab

class BoyerMoore(object):
  """
  Encapsulates pattern and associated Boyer-Moore preprocessing.
  """

  def __init__(self, p, alphabet='ACGT'):
    self.p = p
    self.alphabet = alphabet

    # Create map from alphabet characters to integers
    self.amap = {}
    for i in range(len(self.alphabet)):
      self.amap[self.alphabet[i]] = i

    # Make bad character rule table
    self.bad_char = dense_bad_char_tab(p, self.amap)

    # Create good suffix rule table
    _, self.big_l, self.small_l_prime = good_suffix_table(p)

  
  def bad_character_rule(self, i, c):
    """
    Return # skips given by bad character rule at offset i
    """
    assert c in self.amap
    ci = self.amap[c]
    assert i > (self.bad_char[i][ci]-1)
    return i - (self.bad_char[i][ci]-1)

  def good_suffix_rule(self, i):
    """
    Given a mismatch at offset i, return amount to shift
    as determined by (weak) good suffix rule.
    """
    length = len(self.big_l)
    assert i < length
    if i == length - 1:
      return 0
    i += 1          # i points to leftmost matching position of P
    if self.big_l[i] > 0:
      return length - self.big_l[i]
    return length - self.small_l_prime[i]

  def match_skip(self):
    """
    Return amount to shift in case where P matches T.
    """
    return len(self.small_l_prime) - self.small_l_prime[1]

p = 'ACGGTAA'
alphabet = 'ACGT'
n = n_array(p)
# Create map from alphabet characters to integers
amap = {}
for i in range(len(alphabet)):
  amap[alphabet[i]] = i

# Make bad character rule table
bad_char = dense_bad_char_tab(p, amap)

# Create good suffix rule table
_, big_l, small_l_prime = good_suffix_table(p)

print(amap, bad_char, big_l, small_l_prime)
lp = big_l_prime_array(p, n)
print(big_l_array(p, lp))
print(n)
print(small_l_prime_array(n))

print(z_array(p))
print(p[::-1], z_array(p[::-1])[::-1])

# GCTAGCTC
# TCAA
p = 'TCAA'
p_bm = BoyerMoore(p)
print(p_bm.bad_character_rule(2, 'T'))

# GCCCTAACGACCC
# ACGGTAA
p = 'ACGGTAA'
p_bm = BoyerMoore(p)
print(p_bm.good_suffix_rule(3))

"""#### Boyer-Moore implementation"""

def boyer_moore(p, p_bm, t):
  i = 0
  occurrences = []
  comparison = 0
  alignment = 0
  while i < len(t) - len(p) + 1:
    shift = 1
    mismatched = False
    for j in range(len(p)-1, -1, -1):
      comparison += 1
      if not p[j] == t[i+j]:
        skip_bc = p_bm.bad_character_rule(j, t[i+j])
        skip_gc = p_bm.good_suffix_rule(j)
        print(shift, skip_bc, skip_gc)
        shift = max(shift, skip_bc, skip_gc)
        mismatched = True
        break
    if not mismatched:
      occurrences.append(i)
      skip_gc = p_bm.match_skip()
      print(shift, skip_gc)
      shift = max(shift, skip_gc)
    
    i += shift
    alignment += 1
  return occurrences, comparison, alignment

t = 'GCTACGATCTAGAATCTA'
p = 'TCTA'
p_bm = BoyerMoore(p)
print(p_bm.bad_character_rule(3, 'T'))

print(p_bm.bad_character_rule(3, 'C'))

print(p_bm.good_suffix_rule(3))

print(p_bm.match_skip())

occurrences, count, alignment = boyer_moore(p, p_bm, t)
print(occurrences, count, alignment)

p = 'word'
t = 'there would have been a time for such a word'
lowercase_alphabet = 'abcdefghijklmnopqrstuvwxyz '

p_bm = BoyerMoore(p, lowercase_alphabet)
occurrences, count, alignment = boyer_moore(p, p_bm, t)
print(occurrences, count, alignment)

"""### (2) Implementing a k-mer index"""

import bisect

class Index(object):
  def __init__(self, t, k):
    self.k = k
    self.index = []
    for i in range(len(t) - k + 1):
      self.index.append((t[i:i+k], i))
    self.index.sort()

  def query(self, p):
    kmer = p[:self.k]
    i = bisect.bisect_left(self.index, (kmer, -1))
    hits = []
    while i < len(self.index):
      if self.index[i][0] != kmer:
        break

      hits.append(self.index[i][1])
      i += 1

    return hits

def queryIndex(p, t, index):
  k = index.k
  offsets = []
  for i in index.query(p):
    if p[k:] == t[i+k:i+len(p)]:
      offsets.append(i)

  return offsets

t = 'GCTACGATCTAGAATCTA'
p = 'TCTA'

index = Index(t, 2)

print(queryIndex(p, t, index))

"""### (3) Variations on k-mer indeces"""

help(bisect.bisect_left)

"""### (4) Genome indeces used in research

* How to fit the genome into a compact index so that we can sav memory and we can query more quickly?
* Differences between read and reference occur because of
  1. Sequenccing error
  2. Natural variation

* **Hamming distance**
  For $X$ and $Y$ where $|X|$ = |Y|, hamming distance = minimum # substitutions needed to turn one into other
  $X$: GAGGTAGCGGCGTTTAAC
  $Y$: GTGGTAACGGGGTTTAAC

* **Edit distance (Levenshtein distance)**
  For $X$ and $Y$, edit distance = minimum # edits (substitutions, insertions, deletions) needed to turn one into the other
  $X$: TGGCCGCGCAAAAACAGC
  $Y$: TGACCGCGCAAAACAGC

"""

def naiveHamming(t, p, maxMismatch):
  n = len(t)            # length of the text
  m = len(p)            # length of the query 
                        # initial number of mismatch
  occurrences = []      # index of occurrences of p in t

  for i in range(n - m + 1):
    nmt = 0
    for j in range(m):
      if t[i+j] != p[j]:
        nmt += 1
        if nmt > maxMismatch:
          break

    if nmt <= maxMismatch:
      occurrences.append(i)

  return occurrences

t = 'TCTAGCGCTCTA'
p = 'TCTA'
maxMismatch = 1

occurrences = naiveHamming(t, p, maxMismatch)
print(occurrences)

"""### (5) Pigeonhole principle

* Approximate matching
  **Wanted:** way to apply exact matching algorithms to approximate matching problems
  * If P occurs in T with 1 edit, the $u$ or $v$ appears with no edits

"""

def approximate_match(p, t, n):
  segment_length = int(round(len(p)/(n+1)))
  all_matches = set()
  for i in range(n+1):
    start = i*segment_length
    end = min((i+1)*segment_length, len(p))
    p_bm = BoyerMoore(p[start:end], alphabet='ACGT')
    matches = boyer_moore(p[start:end], p_bm, t)

    for m in matches:
      if m < start or m-start+len(p) > len(t):
        continue
      
      mismatches = 0
      for j in range(0, start):
        if not p[j] == t[m-start+j]:
          mismatches += 1
          if mismatches > n:
            break

      for j in range(end, len(p)):
        if not p[j] == t[m-start+j]:
          mismatches += 1
          if mismatches > n:
            break

      if mismatches <= n:
        all_matches.add(m - start)

  return list(all_matches)

p = 'AACTTG'
t = 'CACTTAATTTG'
print(approximate_match(p, t, 2))

n = 2
round(len(p)/(n+1))