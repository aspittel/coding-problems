"""
Finishes in 0.4s for both small and large inputs. Solved in
competition, but cleaned up after the fact. 

https://codejam.withgoogle.com/codejam/contest/dashboard?c=12224486#s=p1
"""
def clean_input_file(file_name):
	inp = open(file_name)
	inp = inp.read()
	inp = inp.split('\n')
	cases = int(inp[0])
	inp.pop(0)
	inp.pop()
	return inp, cases


def multiply_list(li):
	prod = 1
	for i in li:
		prod *= i
	return prod


def find_probability(performers, probabilities):

	if probabilities.count(0.0) >= performers:
		return 1.0

	role_probs = []
	for i in range(performers):
		min = probabilities.pop(0)
		max = probabilities.pop()
		role_probs.append(1 - min * max)

	return multiply_list(role_probs)


input_file, cases = clean_input_file('B-large-practice.in')
write_file = open('solution.txt', 'w+')

row = 0
for case in range(cases):
	performers = int(input_file[row])
	row += 1
	probabilities = sorted([float(i) for i in input_file[row].split(' ')])
	row += 1
	prob = find_probability(performers, probabilities)
	write_file.write("Case #{}: {}\n".format(case + 1, prob))