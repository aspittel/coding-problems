"""
Factorial digit sum: Project Euler Problem 20

https://projecteuler.net/problem=20

Takes 0.5s on my computer.
"""

def factorial(n):
	if n <= 1:
		return 1

	return n * factorial(n-1)


def sum_digits(n):
	n = list(str(n))
	n = [int(i) for i in n]
	return sum(n)


print(sum_digits(factorial(100)))