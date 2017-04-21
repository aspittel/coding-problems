"""
Several ways to calculate factorials
"""

def factorial(n):
	# Iterative approach
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


def factorial(n):
	# Recursive approach
    if n <= 1:
        return 1
    return n * factorial(n-1)
