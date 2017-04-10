"""
Special Pythagorean triplet: Project Euler Problem 9
Solution in Python

https://projecteuler.net/problem=9

Takes .5s on my computer
"""
def find_triplet(n):
	for a in xrange(1, n):
		for b in xrange(a+1, n):
			c = (a**2 + b**2)**.5
			if a + b + c == float(n):
				return int(a * b * c)

print(find_triplet(1000))