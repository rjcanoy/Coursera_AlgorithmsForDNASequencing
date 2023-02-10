## Preprocessing of the string for Boyer-Moore implementation
import string

## Preprocessing of text
def z_array(s):
  """
  Use Z algorithm to preprocess s
  """

  z = [len(s)] + [0] * (len(s) - 1)

  # Initial comparison: Index = 1
  for i in range(1, len(s)):
    if s[i] == s[i-1]:
      z[1] += 1
    else:
      break

  r, l = 0, 0
  if z[1] > 0:
    r, l = z[1], 1

  # Succeeding comparison: Index = 1 onwards
  for k in range(2, len(s)):
    assert z[k] == 0
    # Case 1
    if k > r:
      for i in range(k, len(s)):
        if s[i] == s[i-k]:
          z[k] += 1
        else:
          break
      r, l = k + z[k] - 1, k

    # Case 2
    else:
      nbeta = r - k + 1
      zkp = z[k-1]
      if nbeta > zkp:
        z[k] = zkp
      else:
        nmatch = 0
        for i in range(r+1, len(s)):
          if s[i] == s[i-k]:
            nmatch += 1
          else:
            break
        l, r = k, r + nmatch
        z[k] = r - k + 1
  
  return z

def n_array(s):
  """
  Compare the N array from the z array.
  """
  return z_array(s[::-1])[::-1]

def big_l_prime_array(p, n):
  """
  Compile L' array using p and N array.
  L'[i] = largest index j less than n such N[i] = |P[i:]|
  """
  lp = [0] * len(p)
  for j in range(len(p) - 1):
    i = len(p) - n[j]
    if i < len(p):
      lp[i] = j + 1

  return lp

def big_l_array(p, lp):
  """
  Compile L array using p and L' array
  L[i] = largest index j less than n such that N[j] >= |P[i:]|
  """
  l = [0] * len(p)
  l[1] = lp[1]
  for i in range(2, len(p)):
    l[i] = max(l[i-1], lp[i])

  return l

def small_l_prime_array(n):
  """
  Compile lp' array using N array.
  """
  small_lp = [0] * len(n)
  for i in range(len(n)):
    if n[i] == i+1:
      small_lp[len(n)-i-1] = i+1
  for i in range(len(n)-2, -1, -1):
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
  i += 1                    # i points to the leftmost matching position of p
  if big_l_prime[i] > 0:
    return length - big_l_prime[i]
  return length - small_l_prime[i]

def good_suffix_match(small_l_prime):
  """
  Given a full match of P to T, return amount to shft as
  determined by good suffix rule.
  """
  return len(small_l_prime) - small_l_prime[1]

def dense_bad_char_tab(p, amap):
  """
  Given pattern string and list with ordered alphabet characters, create
  and return a dense bad character table. Table is indexed by offset
  the by character.
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

  def __init__(self, p, alphabet = 'ACGT'):
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
    assert i > (self.bad_char[i][ci] - 1)
    return i - (self.bad_char[i][ci] - 1)

  def good_suffix_rule(self, i):
    """
    Given a mismatch at offset i, return amount to shift
    as determined by (weak) good suffix rule
    """
    length = len(self.big_l)
    assert i < length
    if i == length - 1:
      return 0
    i += 1                  # i points to leftmost position of P
    if self.big_l[i] > 0:
      return length - self.big_l[i]
    return length - self.small_l_prime[i]

  def match_skip(self):
   """
   Return amount to shift in case where P matches T.
   """
   return len(self.small_l_prime) - self.small_l_prime[1]