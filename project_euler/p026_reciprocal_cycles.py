"""
Reciprocal cycles: Project Euler Problem 26

https://projecteuler.net/problem=26

Takes 0.4s on my computer. Needed help with the formula for 
reciprocal cycles.
"""
def find_max_cycle_len():
	curr_max = 0
	max_i = 0
	for i in xrange(1, 1000):
		length = reciprocal_cycle_len(i)
		if length > curr_max:
			curr_max = length
			max_i = i
	return max_i


def reciprocal_cycle_len(n):
	remainders = {}
	tracker = 1
	position = 0

	while tracker not in remainders:
		remainders[tracker] = position
		tracker = (tracker * 10) % n
		position += 1

	return position - remainders[tracker]


print(find_max_cycle_len())
