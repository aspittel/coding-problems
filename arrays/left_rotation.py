"""
Array left rotation

Question from Cracking the Coding Interview HackerRank.
https://www.hackerrank.com/challenges/ctci-array-left-rotation
"""
def array_left_rotation(a, n_rotations):
    if n_rotations == 0:
        return a
    return array_left_rotation(a[1:] + [a[0]], n_rotations)
    
