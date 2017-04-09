"""
Checks to see if one string is a permutation of another one. 

Problem from Cracking the Coding Interview.
"""
def check_if_perumutation(str_1, str_2):
	"""
	O(N log N) complexity in worst case scenario
	Python's sorted uses a TimSort which is a 
	combination of a merge sort and an insertion sort
	"""
	return sorted(str_1) == sorted(str_2)
