"""
Write a function that replaces spaces in a string with '%20'

From Cracking the Coding Interview
"""
def urlify(str):
	# O(N) complexity
	return str.strip().replace(' ', '%20')

def urlify2(str):
	# Still O(N) complexity, less Pythonic but more universal across languages
	str = list(str)
	for index, char in enumerate(str):
		if char == ' ':
			str[index] = '%20'
	return ''.join(str)


print(urlify('hello world'))
print(urlify2('hello world'))
