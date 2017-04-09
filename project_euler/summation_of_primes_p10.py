"""
Summation of primes: Project Euler Problem 10
Solution in Python

https://projecteuler.net/problem=10

Takes 1.4s on my computer
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

print(sum(list_of_primes(2000000)))