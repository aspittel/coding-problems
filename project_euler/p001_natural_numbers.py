"""
Multiples of 3 and 5: Project Euler Problem 1
Solution in Python

https://projecteuler.net/problem=1

Takes 0.4s on my computer
"""

def sum_natural_numbers_below_n(n):
	# O(N) complexity
	mult_3 = range(3, n, 3)
	mult_5 = range(5, n, 5)
	all_multiples = set(mult_3 + mult_5)
	return sum(all_multiples)

print(sum_natural_numbers_below_n(1000))
