"""
Highly divisible triangular number: Project Euler Problem 12
Solution in Python

https://projecteuler.net/problem=12

Takes 4.5s on my computer
"""
def find_triangle_term(n):
	return n * (n-1) / 2


def get_n_of_divisors(n):
	factors = set()
	for i in xrange(1, int(n**0.5)):
		if n % i == 0:
			factors.add(i)
			factors.add(n/i)
	return len(factors)
 

def find_triangle_with_divisors(n):
 	check = 3
 	divisors = 2
 	while divisors < n:
	 	triangle = find_triangle_term(check)
	 	divisors = get_n_of_divisors(triangle)
		check += 1
	return triangle

print(find_triangle_with_divisors(500))