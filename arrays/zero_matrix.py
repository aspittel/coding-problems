"""
Zeros a row or column of a matrix if there is a zero in it.
"""

def zero_matrix(matrix):
    # Assumes that you are being fed a matrix
    # O(NxM) Complexity 
    row_checks = []
    col_checks = []

    for row_index, row in enumerate(matrix):
        for col_index, item in enumerate(row):
            if item == 0:
                col_checks.append(col_index)
                row_checks.append(row_index)
    
    for row in row_checks:
        matrix[row] = [0] * len(matrix[0])

    for col in col_checks:
        for row in matrix:
            row[col] = 0

    return matrix
