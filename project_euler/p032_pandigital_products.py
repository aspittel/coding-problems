"""
Pandigital products: Project Euler Problem 32

https://projecteuler.net/problem=32

Takes 3.1s on my computer.
"""
prods = set()

for i in range(100):
	for j in range(i, 10000):
		prod = i*j
		pandigits = str(i) + str(j) + str(prod)
		# Check to make sure that the digits are all unique, there are nine of them, and 0 is not a digit
		# therefore making the product pandigital
		# if sorted(pandigits) == '123456789' is cleaner but much less efficient
		if len(set(pandigits)) == len(pandigits) and len(set(pandigits)) == 9 and '0' not in pandigits:
			prods.add(prod)

print(sum(prods))