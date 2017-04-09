"""
Compress string.

From Cracking the Coding Interview.
"""
def compress_string(str):
	# O(N) Complexity
	counter = 0
	new_values = []

	for l1, l2 in zip(str, str[1:] + ' '):
		if l1 == l2:
			counter += 1
		elif counter >= 1:
			counter += 1
			new_values.append('{}{}'.format(l1, counter))
			counter = 0
		else:
			new_values.append(l1 + '1')

	new_values = ''.join(new_values)
	if len(new_values) < len(str):
		return new_values
	else:
		return str
