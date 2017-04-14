"""
Number spiral diagonals: Project Euler Problem 28

https://projecteuler.net/problem=28

Takes 0.5s on my computer.
"""
len_of_squares = list(range(1, 1002, 2))
right_up_diagonal = [n**2 for n in len_of_squares]
len_of_squares.pop(0) # don't duplicate the one in other diagonals
left_up_diagonal = [n**2 - (n-1) for n in len_of_squares]
left_down_diagonal = [n**2 - 2*(n-1) for n in len_of_squares]
right_down_diagonal = [n**2 - 3*(n-1) for n in len_of_squares]

print(sum(left_down_diagonal) + sum(right_down_diagonal) + sum(left_up_diagonal) + sum(right_up_diagonal))