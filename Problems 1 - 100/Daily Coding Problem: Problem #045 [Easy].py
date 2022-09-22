# Good morning! Here's your coding interview problem for today.

# This problem was asked by Two Sigma.

# Using a function rand5() that returns an integer from 1 to 5 (inclusive) with
# uniform probability, implement a function rand7() that returns an integer from 1
# to 7 (inclusive).

import random


"""

we need to compute rand5() twice to cover the range of 7. 
create the smallest 2d array such that there are equal numbers of 1-7
fill the rest with 0

now it would just be throwing darts until we dont get a 0

"""

def rand5():
        return random.randint(1, 5)

def rand7():
        array = [[1,2,3,4,5], [6,7,1,2,3], [4,5,6,7,1], [2,3,4,5,6], [7,0,0,0,0]]
        
        while True:
                i = rand5()
                j = rand5()
                
                if array[i-1][j-1]:
                        return array[i-1][j-1]

print(rand7())