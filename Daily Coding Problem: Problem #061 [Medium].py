# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Implement integer exponentiation. That is, implement the pow(x, y) function,
# where x and y are integers and returns x^y.

# Do this faster than the naive method of repeated multiplication.

# For example, pow(2, 10) should return 1024.

"""

naive method runs in O(n) time where n is the exponent

split exponent into half instead. Now it will run in O(log n)

"""


from typing import *

class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = x
        exponent = n
        if n < 0:
            result = 1/x
            exponent = -n
        
        coeff = 1
        while exponent > 1:
            if exponent % 2 == 0:
                exponent = exponent // 2
                result *= result
            
            else:
                coeff *= result
                result *= result
                exponent = (exponent - 1) // 2
        
        return coeff * result