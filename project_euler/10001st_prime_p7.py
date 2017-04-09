"""
10001st prime product: Project Euler Problem 7
Solution in Python

https://projecteuler.net/problem=7

Takes .9s on my computer
"""

def is_prime(n):
	nums_to_check = range(2, int(n**.5) + 1)
	for i in nums_to_check:
		if n % i == 0:
			return False
	return True

def prime_at_index(idx):
	n_primes = 1
	n = 2
	while n_primes < idx:
		n+=1
		if is_prime(n):
			n_primes += 1
	return n

print(prime_at_index(10001))