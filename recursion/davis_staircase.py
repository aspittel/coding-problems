"""
See how many ways a person can climb a stair case in intervals of 1, 2, or 3 steps

Question from Cracking the Coding Interview HackerRank 
https://www.hackerrank.com/challenges/ctci-recursive-staircase
"""
steps_cache = {1:1, 2:2, 3:4}

def patterns(n):
    if n not in steps_cache:
        steps_cache[n] = patterns(n-1) + patterns(n-2) + patterns(n-3)
    return steps_cache[n]