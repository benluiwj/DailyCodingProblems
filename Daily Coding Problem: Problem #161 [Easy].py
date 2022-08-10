# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given a 32-bit integer, return the number with its bits reversed.

# For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000,
# return 0000 1111 0000 1111 0000 1111 0000 1111.
from typing import *

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        for i in range(32):
                most_sig = n & 1
                result += most_sig * (2 ** (31 - i))
                n = n >> 1
        
        print(result)
        return result


sol = Solution()
sol.reverseBits(4294967293)