"""
Given inputted coins check how many ways an inputted amount can be made from those coins.

Question from Cracking the Coding Interview HackerRank 
https://www.hackerrank.com/challenges/ctci-coin-change
"""

def make_change(coins, n):
    memo = [0 for i in range(n+1)]
    memo[0] = 1
    for coin in coins:
        for check in range(coin, n+1):
            memo[check] += memo[check-coin]
    return memo[n]