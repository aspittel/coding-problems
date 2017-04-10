"""
Names scores: Project Euler Problem 22

https://projecteuler.net/problem=22

Takes 0.5s on my computer.
"""
LETTERS = '-ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Dash takes care of index issue (i.e. A is 1 not 0)

def word_to_number(word):
	score = 0
	for letter in word:
		score += LETTERS.index(letter)
	return score


def names_scores(names):
	score = 0
	curr_name = 1
	for name in names:
		score += (curr_name * word_to_number(name))
		curr_name += 1
	return score

names = open('/Users/aspittel/Desktop/p022_names.txt')
names = names.read()

# data clean up 
names = names.replace('"', '')
names = names.split(',')
names = sorted(names)

print names_scores(names)