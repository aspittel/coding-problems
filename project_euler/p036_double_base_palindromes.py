"""
Double-base palindromes: Project Euler Problem 36

https://projecteuler.net/problem=36

Takes 1.8s on my computer.
"""
def is_palindrome(n):
	return n == n[::-1]


def find_double_base_palindromes(n):
	double_base_palindromes = []
	for i in range(n+1):
		if is_palindrome(str(i)) and is_palindrome("{0:b}".format(i)):
			double_base_palindromes.append(i)
	return double_base_palindromes


print(sum(find_double_base_palindromes(1000000)))