# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0,
# using only mathematical or bit operations. You can assume b can only be 1 or 0.

"""

without contraints

if b == 1:
	return x
else:
	return y
 
when b is 0, return y
when b is 1, return x
multiply x with b and multiply y with 1 - b then add them together

"""
def return_xy(x,y,b):
        return (x * b) | (y * (1-b))