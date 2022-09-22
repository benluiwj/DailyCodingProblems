# Good morning! Here's your coding interview problem for today.

# This problem was asked by Two Sigma.

# Using a function rand7() that returns an integer from 1 to 7 (inclusive) with
# uniform probability, implement a function rand5() that returns an integer from 1
# to 5 (inclusive).

from random import randint

"""
since probability is uniform, can just return when result of ran7 is 1 through 5
"""

def rand7():
        return randint(1,7)

def rand5():
        r = rand7()
        if 1 <= r <= 5:
                return r
        
        return rand5()