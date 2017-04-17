"""
Draws a pyramid with an inputted number of rows.

https://www.hackerrank.com/challenges/staircase?h_r=next-challenge&h_v=zen
"""

def create_pyramid(n):
    counter = 1
    while counter <= n:
        hashes = ['#'] * counter
        spaces = [' '] * (n - counter)
        print(''.join(spaces + hashes))
        counter += 1