# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given a positive integer n, find the smallest number of squared integers which
# sum to n.

# For example, given n = 13, return 2 since 13 = 32 + 22 = 9 + 4.

# Given n = 27, return 3 since 27 = 32 + 32 + 32 = 9 + 9 + 9.

from cmath import sqrt
from typing import *

"""

get all the squares up to n
breadth first search to find the result, subtracting them along the way

create an array of the squares up to n

create an array from 1 to n

to get the ans for the current:
if the current is perfect square, answer is 1

otherwise, get the closest perfect square to itself
to get the closest square to itself, check head of the square list
if the number itself is perfect, pop the head.
divide this and get the quotient and remainder

the dp[i] = quotient + dp[remainder]

return the last

to reduce space usage,

use an inner loop to check the squares and compare the minimum as long as the difference is greater than or equal to 0. Current implementation uses more space and is slightly slower since we iterate through all the squares. 

"""

import math

class Solution:
    def numSquares(self, n: int) -> int:
        upper_bound = math.floor(math.sqrt(n))
        
        dp = [[0 for _ in range(n + 1)] for _ in range(upper_bound)]
        
        # since 1 is a square, all numbers can form sums of 1 and the answer is the number itself
        for i in range(n + 1):
            dp[0][i] = i
            
        for i in range(upper_bound):
            dp[i][1] = 1
        
        for col in range(1, n + 1):
            for row in range(1, upper_bound):
                square = (row + 1) ** 2
                # if the square is greater than the number, just return the previous
                if square > col:
                    dp[row][col] = dp[row - 1][col]
                
                elif square == col:
                    dp[row][col] = 1
                
                else:
                    quotient = col // square
                    remainder = col % square
                    dp[row][col] = min(dp[row - 1][col], quotient + dp[-1][remainder])
        
        return dp[-1][-1]

sol = Solution()
sol.numSquares(12)