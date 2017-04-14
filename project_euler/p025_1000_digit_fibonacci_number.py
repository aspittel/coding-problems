"""
1000-digit Fibonacci number: Project Euler Problem 25

https://projecteuler.net/problem=25

Takes 0.5s on my computer.
"""

def fibonacci_sequence(digits):
	n1 = 1
	n2 = 1
	index = 2
	while len(str(n2)) < digits:
		n1, n2 = n2, n1 + n2
		index += 1
	return index

print fibonacci_sequence(1000)
