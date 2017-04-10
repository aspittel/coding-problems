"""
Power digit sum: Project Euler Problem 16
Solution in Python

https://projecteuler.net/problem=16

Takes 0.4s on my computer
"""
def power_digit_sum(n):
	power = str(2**n)
	_sum = 0
	for i in power:
		_sum += int(i)
	return _sum

print(power_digit_sum(1000))