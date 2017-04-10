"""
Even Fibonacci numbers: Project Euler Problem 2
Solution in Python

https://projecteuler.net/problem=2

Takes 0.4s on my computer
"""
def fibonacci_sequence(n):
	numbers = [0, 1]

	while numbers[-1] < n:
		numbers.append(numbers[-1] + numbers[-2])

	return numbers

def sum_even_fibonacci_numbers(n):
	# O(N) Complexity
	sequence = fibonacci_sequence(n)
	sequence = [n for n in sequence if n % 2 == 0]
	return sum(sequence)

print(sum_even_fibonacci_numbers(4000000))