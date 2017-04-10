"""
Non-abundant sums: Project Euler Problem 23

https://projecteuler.net/problem=23

Takes 4.0s on my computer.
"""
LIMIT = 28123

def get_divisors(n):
	divisors = set([1])
	for i in xrange(2, int(n**0.5)+1):
		if n % i == 0:
			divisors.add(i)
			divisors.add(n/i)
	return divisors


def find_abundant_numbers(n):
	abundant_numbers = set()
	for i in xrange(1, n):
		divisors = get_divisors(i)
		if sum(divisors) > i:
			abundant_numbers.add(i)
	return list(abundant_numbers)


def find_sums_in_list(li):
	sums = set()
	for index, i in enumerate(li):
		for j in li[index:]:
			sums.add(i+j)
	return sums


def find_not_in_li(li, limit):
	not_in = set()
	li = set(li)
	for i in xrange(1, limit+1):
		if i not in li:
			not_in.add(i)
	return not_in


def find_sum_nonabundant_numbers(limit):
	abundant_numbers = find_abundant_numbers(limit+1)
	sums = find_sums_in_list(abundant_numbers)
	not_in_li = find_not_in_li(sums, limit)
	return sum(not_in_li)

print find_sum_nonabundant_numbers(LIMIT)