"""
Works in 0.4s for each small problem set, 0.7s for the large. Solved within competition, cleaned up after.

https://code.google.com/codejam/contest/3264486/dashboard#s=p2
"""
from math import floor, ceil

def clean_input_file(file_name):
	inp = open(file_name)
	inp = inp.read()
	inp = inp.split('\n')
	cases = int(inp[0])
	inp.pop(0)
	inp.pop()
	return inp, cases


def find_min_stall(stalls, people):
	nth_powers = []
	n = 0
	while sum(nth_powers) < people:
		nth_powers.append(2**n)
		n+=1

	sum_powers = sum(nth_powers)
	remaining_n = stalls - sum_powers
	key_power = nth_powers[-1]

	remaining_people = people - key_power
	rem = remaining_n % key_power
	div = (stalls / key_power) - 1

	product = div * rem
	remainder = remaining_n - product
	people_needed = key_power - rem

	if remaining_people > rem:
		sol = float(remainder / people_needed)
	else:
		sol = float(div)

	_max = int(ceil(sol/2))
	_min = int(floor(sol/2))
	return '{} {}'.format(_max, _min)


input_file, cases = clean_input_file('C-large-practice.in')

write_file = open('solution.txt', 'w+')
for idx, n in enumerate(input_file):
	n = n.split(' ')
	write_file.write("Case #{}: {}\n".format(idx + 1, find_min_stall(int(n[0]), int(n[1]))))
