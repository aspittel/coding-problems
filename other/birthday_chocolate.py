"""
Get the number of ways m pieces of a chocolate bar can add up to d

From https://www.hackerrank.com/challenges/the-birthday-bar?h_r=next-challenge&h_v=zen
"""

def getWays(squares, d, m):
    ways = 0
    for i in range(len(squares) - m + 1):
        s = 0
        for j in range(m):
            s += squares[i + j]
        if d == s: ways += 1
    return ways
