"""
Lattice paths: Project Euler Problem 15

https://projecteuler.net/problem=15

Takes 0.4s on my computer. Had to refresh myself on combinatorics.
"""

def lattice_paths(n):
	n_paths = 1
	for i in range(1, n+1):
		n_paths = n_paths * (n + i)/i
	return n_paths

print(lattice_paths(20))