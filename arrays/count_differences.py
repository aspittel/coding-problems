"""
Count the number of changes needed to make two words anagrams of one another.

https://www.hackerrank.com/challenges/ctci-making-anagrams
"""
from collections import Counter

def number_needed(a, b):
	# O(N) Complexity
    a_counter = Counter(a)
    b_counter = Counter(b)
    
    differences = 0
    
    for l in a_counter:
        if l in b_counter:
            if a_counter[l] != b_counter[l]:
                differences += abs(a_counter[l] - b_counter[l])
        else:
            differences += a_counter[l]
            
    for l in b_counter:
        if l not in a_counter:
            differences += b_counter[l]
    
    return differences
