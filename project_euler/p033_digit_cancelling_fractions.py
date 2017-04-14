"""
Digit Cancelling Fractions: Project Euler Problem 33

https://projecteuler.net/problem=33

Takes 0.4s on my computer.
"""

def check_if_digit_cancelling(i, j):
	i_digits = [i  % 10, i / 10]
	j_digits = [j % 10, j / 10]

	for digit in i_digits:
		if digit in j_digits and digit != 0 and digit != 5:
			i_digits.remove(digit)
			j_digits.remove(digit)

			if i_digits[0] != 0 and j_digits[0] != 0:
				if i_digits[0] / float(j_digits[0]) == i / float(j):
					return (i_digits[0] / float(j_digits[0]))

digit_cancelling = []
for i in range(10, 101):
	for j in range(i + 1, 101):
		check = check_if_digit_cancelling(i, j)
		if check:
			digit_cancelling.append(check)

prod = 1
for i in digit_cancelling:
	prod *= i

print(prod)