"""
Takes 0.4s for small set and 0.5s for large set on my computer. Solved in
competition, but cleaned up after the fact. 

https://codejam.withgoogle.com/codejam/contest/12224486/dashboard#s=a&a=0
"""
def clean_input_file(file_name):
	inp = open(file_name)
	inp = inp.read()
	inp = inp.split('\n')
	cases = int(inp[0])
	inp.pop(0)
	inp.pop()
	return inp, cases


def get_seat_positions(seat_nums):
	items = []
	already_in = []

	for seat_num in seat_nums:
		if not seat_num in already_in:
			if seat_num[0] == seat_num[1]:
				items.append(seat_num[0])
			else:
				items.extend(seat_num)
		already_in.append(seat_num)

	return items.count(max(set(items), key=items.count))


input_file, cases = clean_input_file('A-large-practice.in')
write_file = open('solution.txt', 'w+')

row = 0

for case in range(cases):
	case_info = input_file[row].split(' ')
	friends = int(case_info[0])
	seats = int(case_info[1])

	seat_nums = []
	for _ in range(friends):
		row += 1
		seat = input_file[row].split(' ')
		seat_nums.append([int(i) for i in seat])

	write_file.write("Case #{}: {}\n".format(case + 1, get_seat_positions(seat_nums)))
	row += 1
