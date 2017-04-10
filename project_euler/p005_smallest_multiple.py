"""
Smallest multiple: Project Euler Problem 5
Solution in Python

https://projecteuler.net/problem=5

Originally brute forced this which took ~75s. Adapted code from 
http://stackoverflow.com/questions/147515/least-common-multiple-for-3-or-more-numbers to Python 
and took 0.4s
"""

def greatest_common_denominator(a, b):
    while b:      
        a, b = b, a % b
    return a


def least_common_multiple(a, b):
	return (a * b) / greatest_common_denominator(a, b)


def least_common_multiple_range(li):
	if len(li) == 2:
		return least_common_multiple(li[0], li[1])
	else:
		check = li.pop()
		return least_common_multiple(check, least_common_multiple_range(li))


print least_common_multiple_range(range(1, 21))