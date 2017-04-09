"""
Largest palindrome product: Project Euler Problem 4
Solution in Python

https://projecteuler.net/problem=4

Takes .9s on my computer
"""

def palindrome_number():
	_range = xrange(100, 1000)
	palindrome = None
	for i in _range:
		for j in _range:
			prod = i * j
			if str(prod) == str(prod)[::-1]:
				if prod > palindrome:
					palindrome = prod
	return palindrome

print(palindrome_number())