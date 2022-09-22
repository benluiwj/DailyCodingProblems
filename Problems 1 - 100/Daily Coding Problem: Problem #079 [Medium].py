# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given an array of integers, write a function to determine whether the array
# could become non-decreasing by modifying at most 1 element.

# For example, given the array [10, 5, 7], you should return true, since we can
# modify the 10 into a 1 to make the array non-decreasing.

# Given the array [10, 5, 1], you should return false, since we can't modify any
# one element to get a non-decreasing array.

from typing import *

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        forward_change = 0
        forward_curr = nums[0]
        
        for i in range(len(nums)-1):
            forward_curr = max(nums[i], forward_curr)
            next = nums[i+1]
            
            if forward_curr > next:
                forward_change += 1
            

            
        
        backward_count = 0
        backward_curr = nums[-1]
        
        for i in range(len(nums)-1, 0, -1):
            backward_curr = min(nums[i], backward_curr)
            prev = nums[i-1]
            
            if backward_curr < prev:
                backward_count += 1
            
            
        
        return min(backward_count, forward_change) <= 1

sol = Solution()
assert sol.checkPossibility([1,5,4,6,7,10,8,9]) == False
assert sol.checkPossibility([3,4,2,3]) == False
assert sol.checkPossibility([5,7,1,8]) == True