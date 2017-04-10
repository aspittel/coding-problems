"""
Largest prime factor: Project Euler Problem 3 
Solution in Python

https://projecteuler.net/problem=3

Takes 0.7s on my computer.
"""

def list_of_primes(n):
	not_prime = set() # In is O(1) rather than O(N)
	primes = set()
	for i in xrange(2, n+1):
		if i not in not_prime:
			primes.add(i)
			# Adds multiples of the number to the set of checked values
			# i * (i-1) etc. are already updated so starts at i*i
			not_prime.update(range(i*i, n+1, i))
	return primes


def get_factors(n):
	factors = set()
	for i in xrange(1, int(n**0.5)):
		if n % i == 0:
			factors.add(i)
			factors.add(n/i)
	return list(factors)


def get_prime_factors(n):
	factors = sorted(get_factors(n), reverse=True)
	primes = list_of_primes(factors[0])
	for factor in factors:
		if factor in primes:
			return factor
	else:
		return None

print(get_prime_factors(13195))
