"""
Circular Primes: Project Euler Problem 34

https://projecteuler.net/problem=34

Takes 1.9s on my computer.
"""
def list_of_primes(n):
	not_prime = set()
	primes = set()
	for i in xrange(2, n+1):
		if i not in not_prime:
			primes.add(i)
			not_prime.update(range(i*i, n+1, i))
	return primes


def is_circular_prime(n, primes):
	n = str(n)
	for i in range(len(n)):
		new_n = int(n[i:] + n[:i])		
		if new_n not in primes:
			return False
	return True


def get_circular_primes(n):
	primes = list_of_primes(n)
	circular_primes = []
	for i in primes:
		if is_circular_prime(i, primes):
			circular_primes.append(i)
	return circular_primes


print(len(get_circular_primes(1000000)))