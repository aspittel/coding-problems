"""
See if a word is available in the magazine to use for a ransom note.

https://www.hackerrank.com/challenges/ctci-ransom-note
"""
from collections import Counter

def ransom_note(magazine, ransom):
    magazine_counter = Counter(magazine)
    ransom_counter = Counter(ransom)
    for word in ransom_counter:
        if word not in magazine:
            return False
        elif ransom_counter[word] > magazine_counter[word]:
            return False
    return True
