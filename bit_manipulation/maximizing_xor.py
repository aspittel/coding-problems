"""
Returns the maximum XOR in a range.

From https://www.hackerrank.com/challenges/maximizing-xor/submissions/code/43243551
"""

def maxXor(l, r):
  _max = 0
  for x in range(l, r+1):
    for y in range(x, r+1):
        _max = max(_max, x^y)
  return _max
