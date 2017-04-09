"""
Check if a string contains only unique characters.
"""

def check_if_unique(str):
	"""
	Simple implementation in O(N) time. List to set conversion is O(N), len(list) 
	function is O(1).
	"""
	return len(set(str)) == len(str)


def check_if_unique(str):
	"""
	Runs in O(N^2) time, but doesn't use any additional data structures. Checking
	if an item is in a list (here a string) is more costly than checking if an item 
	is in a set.
	"""
	unique_str = ''
	for char in str:
		if char in unique_str:
			return False
		else:
			unique_str += char
	return True