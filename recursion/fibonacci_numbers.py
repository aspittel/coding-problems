"""
Generate the n-th number of the fibonacci sequence.

Question from Cracking the Coding Interview HackerRank 
https://www.hackerrank.com/challenges/ctci-fibonacci-numbers
"""
def fibonacci(n):
	if n == 0 or n == 1:
		return n
	return fibonacci(n-1) + fibonacci(n-2)