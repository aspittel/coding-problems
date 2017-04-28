"""
Count the number of valleys in a hike.

From https://www.hackerrank.com/challenges/counting-valleys.
"""

def count_valleys(steps):
    elevation = 0
    valley_count = 0
    in_valley = False
    for step in steps:
        if step == 'U': 
            elevation += 1
            if elevation >= 0:
                in_valley = False
        elif step == 'D': 
            elevation -= 1
            if elevation < 0 and not in_valley:
                in_valley = True
                valley_count += 1
    return valley_count