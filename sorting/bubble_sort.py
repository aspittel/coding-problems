"""
Python implementation of a bubble sort.

From https://www.hackerrank.com/challenges/ctci-bubble-sort/submissions/code/42625700
"""

def bubble_sort(arr):
    all_swaps = 0
    for i in range(0, len(arr)):
        swaps = 0
        for j in range(0, n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
        all_swaps += swaps
        if swaps == 0:
            break
    return all_swaps, arr[0], arr[-1]
