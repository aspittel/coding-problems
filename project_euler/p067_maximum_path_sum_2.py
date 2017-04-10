"""
Maximum path sum II: Project Euler Problem 67

https://projecteuler.net/problem=67

Takes 0.4s on my computer.
"""
def find_greatest_path(triangle):
	if len(triangle) == 1:
		return triangle[0][0]

	bottom = triangle[-1]
	curr_row = triangle[-2]

	for index, item in enumerate(curr_row):
		path_one = int(item) + int(bottom[index])
		path_two = int(item) + int(bottom[index+1])
		curr_row[index] = max(path_one, path_two)

	triangle.pop()
	return find_greatest_path(triangle)

triangle = open('/Users/aspittel/Desktop/p067_triangle.txt')
triangle = triangle.read()
triangle = triangle.split('\n')
triangle = [row.split(' ') for row in triangle]
triangle.pop()

print(find_greatest_path(triangle))