"""
Return the max and min possible sums of n-1 integers.

From https://www.hackerrank.com/challenges/mini-max-sum/submissions/code/42826333.
"""

def max_and_min_sum(li):
    li = sorted(li)
    return sum(li[:-1]), sum(li[1:])
