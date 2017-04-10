"""
Number letter counts: Project Euler Problem 17

https://projecteuler.net/problem=17

Takes 0.4s on my computer.
"""
number_words = {
	1: 'one',
	2: 'two',
	3: 'three',
	4: 'four',
	5: 'five',
	6: 'six',
	7: 'seven',
	8: 'eight',
	9: 'nine',
	10: 'ten',
	11: 'eleven',
	12: 'twelve',
	13: 'thirteen',
	14: 'fourteen',
	15: 'fifteen',
	16: 'sixteen',
	17: 'seventeen',
	18: 'eighteen',
	19: 'nineteen',
	20: 'twenty',
	30: 'thirty',
	40: 'fourty',
	50: 'fifty',
	60: 'sixty',
	70: 'seventy',
	80: 'eighty',
	90: 'ninety',
	1000: 'onethousand'
}

def number_to_words(number):
	if number in number_words:
		return number_words[number]
	elif number < 100:
		return number_words[(number // 10) * 10] + number_words[number % 10]
	else:
		word = number_words[number // 100] + 'hundred'
		if number % 100 != 0:
			word += 'and'
			word += number_to_words(number % 100)
		return word


def count_letters_in_range(n):
	letter_count = 0
	for i in xrange(1, n+1):
		letter_count += len(number_to_words(i))
	return letter_count


print(count_letters_in_range(1000))