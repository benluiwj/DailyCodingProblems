# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given an array of integers where every integer occurs three times except for one
# integer, which only occurs once, find and return the non-duplicated integer.

# For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13],
# return 19.

# Do this in O(N) time and O(1) space.
from typing import *

"""

without O(1) space constraint, create a table with the frequency. Find the one with only 1 frequency.

Do perform in O(1) -> some form of bit manipulation.

if 2 nums: a xor b xor a xor c xor c -> b
a xor b xor a -> b
a xor b xor a xor a -> a xor b
 
xor 2 numbers -> cancel bits with even number of 1s

xor 3 numbers -> cancel bits with multiple number of 3 1s


"""

class Solution:
        def singleNumber(self, nums: List[int]) -> int:
                bits = [0 for _ in range(32)]
                
                for num in nums:
                        for i in range(31, -1, -1):
                                most_significant = num % 2
                                bits[i] += most_significant
                                num = num >> 1
                
                result = 0
                
                for i in range(31, -1, -1):
                        if bits[i] % 3 != 0:
                                result += 2 ** (31 - i)
                
                return result
        

sol = Solution()

assert sol.singleNumber([13, 19, 13, 13]) == 19