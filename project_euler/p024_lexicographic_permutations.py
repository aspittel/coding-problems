"""
Non-abundant sums: Project Euler Problem 24

https://projecteuler.net/problem=24

Takes 0.4s on my computer.
"""
from math import floor 

def factorial(n):
	if n <= 1:
		return 1
	return n * factorial(n-1)


def get_permutation(digits, n):

	if len(digits) <= 1:
		return str(digits[0])

	n_permutations = factorial(len(digits) - 1)
	index = int(floor(n / n_permutations))
	permutation = digits[index]
	
	digits.pop(index)

	return str(permutation) + get_permutation(digits, n % n_permutations)

print get_permutation([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1000000-1) # minus one for indexing purposes