"""
Digit fifth powers: Project Euler Problem 29

https://projecteuler.net/problem=29

Takes 2.9s on my computer.
"""

fifth_powers = []
MAX = 6*(9**5)

for i in range(2, MAX):
	str_i = str(i)
	_sum = 0
	for j in str_i:
		_sum += int(j)**5
	if _sum == i:
		fifth_powers.append(i)

print(sum(fifth_powers))