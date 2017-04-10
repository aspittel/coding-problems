"""
Longest Collatz sequence: Project Euler Problem 12
Solution in Python

https://projecteuler.net/problem=2

Takes 0.4s on my computer
"""
collatz_cache = {}

def next_collatz(n):
	if n % 2 == 0:
		return n/2
	else:
		return (3*n) + 1


def collatz_sequence(n):
	if n == 1:
		return 1

	if n in collatz_cache:
		return collatz_cache[n]

	else:
		collatz_cache[n] = 1 + collatz_sequence(next_collatz(n))

	return collatz_cache[n]


def find_longest_collatz_sequence(n):
	longest_sequence = 1
	n_longest_sequence = 1
	for i in xrange(1, n):
		curr_collatz = collatz_sequence(i)
		if curr_collatz > longest_sequence:
			longest_sequence = curr_collatz
			n_longest_sequence = i
	return n_longest_sequence


print(find_longest_collatz_sequence(1000000))
