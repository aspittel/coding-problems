"""
Distinct Powers: Project Euler Problem 29

https://projecteuler.net/problem=29

Takes 0.4s on my computer.
"""
powers = set()

for i in range(2, 101):
	for j in range(2, 101):
		powers.add(i**j)
		
print(len(powers))