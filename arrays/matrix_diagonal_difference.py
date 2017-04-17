"""
Finds the differences of the diagonals of a matrix.

Question from HackerRank algorithm challenges.
https://www.hackerrank.com/challenges/diagonal-difference
"""
def matrix_diagonal_difference(a, n):
    diag_one = []
    while len(diag_one) < n:
        coord = len(diag_one)
        diag_one.append(a[coord][coord])
    
    diag_two = []
    coord = n - 1
    while len(diag_two) < n:
        diag_two.append(a[len(diag_two)][coord])
        coord -=1
        
    return abs(sum(diag_one) - sum(diag_two))
