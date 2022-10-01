# Good morning! Here's your coding interview problem for today.

# This problem was asked by Pinterest.

# Given an integer list where each number represents the number of hops you can
# make, determine whether you can reach to the last index starting at index 0.

# For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
from typing import *

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumps = nums[0]
        if jumps == 0:
            return False
        
        for i in range(1, len(nums)):
            jumps -= 1
            jumps = max(nums[i], jumps)
            
            if not jumps:
                return False
            
        return jumps >= 0