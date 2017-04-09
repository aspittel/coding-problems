"""
Find the difference between two arrays with one different integer.
"""

def finder_improved(arr1, arr2):
	# O(N Log N)
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    
    for index in range(len(arr1)):
        if arr1[index] != arr2[index]:
            return arr1[index]
