"""
From http://www.codewars.com/kata/simple-pig-latin/python
"""

from string import punctuation


def pig_it(text):
    return ' '.join(word[1:] + word[0] + 'ay' if word not in punctuation else word for word in text.split(' '))
