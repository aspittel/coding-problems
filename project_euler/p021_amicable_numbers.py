"""
Amicable numbers: Project Euler Problem 21

https://projecteuler.net/problem=21

Takes 0.6s on my computer.
"""
def get_divisors(n):
	divisors = set([1])
	for i in xrange(2, int(n**0.5)+1):
		if n % i == 0:
			divisors.add(i)
			divisors.add(n/i)
	return divisors


def get_amicable_numbers(n):
	amicable_numbers = set()
	for i in xrange(1, n):
		divisor_sum = sum(get_divisors(i))
		amicable_sum = sum(get_divisors(divisor_sum))
		if amicable_sum == i and divisor_sum != i:
			amicable_numbers.add(i)
			amicable_numbers.add(divisor_sum)
	return sum(amicable_numbers)


print(get_amicable_numbers(10000))

