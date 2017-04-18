"""
Two algorithms for finding primes -- the first uses cacheing, the second is 
more efficient for finding one prime number.

Inspired by https://www.hackerrank.com/challenges/ctci-big-o
"""

def list_of_primes(n):
	primes = set()
	not_prime = set()

	for i in range(2, n+1):
		if i not in not_prime:
			primes.add(i)
			# Adds multiples of the number to the set of checked values
			# i * (i-1) etc. are already updated so starts at i*i
			not_prime.update(range(i*i, n+1, i))

	return primes


def check_if_prime(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    
    for i in range(3, int(n**.5) + 1):
        if n % i == 0:
            return False
    
    return True
