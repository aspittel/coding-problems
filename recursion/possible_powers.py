"""
Finds the number of ways a number can be comprised of integers to the nth power. 

From https://www.hackerrank.com/challenges/the-power-sum
"""
def possible_powers_sum(n, possible_powers):
    if n == 0: return 1
    if n < 0 or not possible_powers: return 0
    return possible_powers_sum(n-possible_powers[0], possible_powers[1:]) + possible_powers_sum(n, possible_powers[1:])
    
    
def powers(n, power):
    return [n**power for n in range(1, int(n**(1/power)+1))]


def possible_powers(n, power):
    return possible_powers_sum(n, powers(n, power))


print(possible_powers(10, 2))