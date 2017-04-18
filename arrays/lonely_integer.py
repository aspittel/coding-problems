"""
Find the element in an array that only occurs once

from https://www.hackerrank.com/challenges/ctci-lonely-integer
"""

from collections import Counter

def lonely_integer(a):
    a_counter = Counter(a)
    for l, count in a_counter.items():
        if count == 1:
            return l
