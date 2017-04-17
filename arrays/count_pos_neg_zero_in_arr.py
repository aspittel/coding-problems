"""
Returns the ratio of positive, negative, and zero numbers within an array

https://www.hackerrank.com/challenges/plus-minus?h_r=next-challenge&h_v=zen
"""
def ratio_pos_neg_zero(arr, n):
    pos = len([n for n in arr if n > 0])
    neg = len([n for n in arr if n < 0])
    zero = len([n for n in arr if n == 0])
    return pos/float(n), neg/float(n), zero/float(n)