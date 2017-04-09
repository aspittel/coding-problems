"""
Check to see if two strings are anagrams of one another.

Question from Python for Data Structures Udemy Course.
"""

def create_counter(s):
	# Could also use collections.Counter
    counter = {}
    for letter in s:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
    return counter


def anagram(string_1, string_2):
#   O(N) Complexity
    string_1 = string_1.replace(' ', '').lower()
    string_2 = string_2.replace(' ', '').lower()

    counter1 = create_counter(string_1)
    counter2 = create_counter(string_2)

    for letter in counter1:
        if letter in counter2:
            if counter1[letter] != counter2[letter]:
                return False
        else:
            return False
    return True