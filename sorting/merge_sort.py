def merge_sort(li):
	if len(li) <= 1: return li
	middle = len(li) / 2
	left = li[:middle]
	right = li[middle:]
	return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
	result = []
	while left or right:
		if left and right:
			if left[0] < right[0]:
				result.append(left.pop(0))
			else:
				result.append(right.pop(0))
		elif left:
			result.append(left.pop(0))
		else:
			result.append(right.pop(0))
	return result
