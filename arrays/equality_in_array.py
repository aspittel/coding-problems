"""
What is the lowest number of deletions that someone can make to have an array with all of the same elements?

From https://www.hackerrank.com/challenges/equality-in-a-array
"""
from collections import Counter

def n_deletions(li):
	c = Counter(li).most_common(1)[0][1]
	return len(li) - c

print(n_deletions([5, 5, 5, 3, 1]))