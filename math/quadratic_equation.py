def find_quadratic(a, b, c):
	n = (b**2 - (4*a*c))**.5
	pos = -(b) + n
	neg = -(b) - n
	return (pos//(2*a), neg//(2*a))

print find_quadratic(2, 10, 8)