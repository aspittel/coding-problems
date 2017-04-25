def find_max_subarray(arr):
	curr_max = 0
	curr_value = 0

	for val in arr:
		curr_sum = curr_value + val
		
		if curr_sum > 0:
			curr_value = curr_sum
		else:
			curr_value = 0

		if curr_value > curr_max:
			curr_max = curr_value

	if curr_max > 0:
		return curr_max
	
	else:
		# Control for all negative array
		return max(arr)
