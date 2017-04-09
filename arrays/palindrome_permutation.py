"""
Check to see if a string can be rearranged as a palindrome.

From Cracking the Coding Interview.
"""

from collections import Counter

def check_if_palindrome_permutation(str):
	# O(N) complexity
	str = str.replace(' ', '')
	n = len(str)
	letter_counts = Counter(str)
	n_odds = 0
	is_palindrome_permutation = True

	# Count how many letters appear an odd number of times
	for count in letter_counts.values():
		if count % 2 != 0:
			n_odds += 1

	# If the word has even length, then each letter must appear an even number of times
	if n % 2 == 0:
		if n_odds > 0:
			is_palindrome_permutation = False

	# If the word has odd length, than one letter can appearn an odd number of times
	elif n_odds > 1:
		is_palindrome_permutation = False
	return is_palindrome_permutation

