"""
Counting Sundays: Project Euler Problem 19

https://projecteuler.net/problem=19

Takes 0.4s on my computer.
"""
from datetime import datetime

def count_sundays_in_20th_century():
	count = 0
	for year in range(1901, 2001):
		for month in range(1, 13):
			if datetime(year, month, 1).weekday() == 6:
				count += 1
	return count

print count_sundays_in_20th_century()