"""
Quadratic Primes: Project Euler Problem 27

https://projecteuler.net/problem=27

Takes 0.4s on my computer.
"""

from itertools import combinations

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


def find_quadratic_primes(n):
	primes = list_of_primes(n)
	max_primes = 0
	max_prod = 0
	combos = combinations(primes, 2)
	for combo in combos:
		i = 1
		is_prime = True
		while is_prime:
			checker = (i*i) - (min(combo) * i) + max(combo)
			if checker in primes:
				i += 1
			else:
				is_prime = False
		if i > max_primes:
			max_primes = i
			max_prod = -(combo[0] * combo[1])
	return max_prod

print(find_quadratic_primes(1000))
