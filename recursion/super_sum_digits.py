"""
Keep summing the digits of a number until there is only one digit left.

from https://www.hackerrank.com/challenges/recursive-digit-sum/
"""
def sum_digits(n):
    _sum = 0
    for d in n:
        _sum += int(d)
    return str(_sum)


def super_sum_digits(n):
    if len(n) <= 1: return n
    return super_sum_digits(sum_digits(n))
    

def get_super_sum(n, k):
	initial_n = super_sum_digits(n)
	return super_sum_digits(initial_n*k)
