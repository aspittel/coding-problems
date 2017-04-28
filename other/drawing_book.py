"""
Given a page number and a book length, find the minimum number of page flips to get to a given page.

From https://www.hackerrank.com/challenges/drawing-book
"""

from math import floor 

def solve(n, p):
    return min(floor(p/2), floor((n-p)/2))
