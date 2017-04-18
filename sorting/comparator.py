"""
Sorts two values based on score and name.

From https://www.hackerrank.com/challenges/ctci-comparator-sorting.
"""

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return self.name + ' ' + str(self.score)
        
    def comparator(a, b):
        if a.score == b.score:
            return -1 if a.name < b.name else 1
        else:
            return -1 if a.score > b.score else 1