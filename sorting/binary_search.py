def binary_search(li, item, first=0, last=None):
	if not last:
		last = len(li)

	midpoint = (last - first) / 2 + first

	if li[midpoint] == item:
		return midpoint

	elif li[midpoint] > item:
		return binary_search(li, item, first, midpoint)

	else:
		return binary_search(li, item, midpoint, last)

print(binary_search([0, 5, 10, 20, 25, 50], 20))