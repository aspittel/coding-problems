"""
Takes an integer and flips it's 32 bit value and then returns as an integer value.

From https://www.hackerrank.com/challenges/flipping-bits
"""
def convert_to_32(i):
    return "{:032b}".format(i)


def flip(i):
    flipped = ''
    for l in i:
        flipped += '1' if l == '0' else '0'
    return flipped
  

def convert_to_int(i):
    return(int(i, 2))


def flip_bits(i):
	i = convert_to_32(i)
	i = flip(i)
	return convert_to_int(i)