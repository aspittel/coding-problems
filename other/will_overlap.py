'''
Checks to see if, given two starting points and two velocities, two kangaroos will be at the same place
at the same time.

From https://www.hackerrank.com/challenges/kangaroo
'''
def will_overlap(x1, v1, x2, v2):
    if v2 >= v1: return False
    while x1 < x2:
        x1 += v1
        x2 += v2
        if x1 == x2: return True
    return False
