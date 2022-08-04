# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given an array of strictly the characters 'R', 'G', and 'B', segregate the
# values of the array so that all the Rs come first, the Gs come second, and the
# Bs come last. You can only swap elements of the array.

# Do this in linear time and in-place.

# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should
# become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

from typing import *

"""

Similar to sorting in place. Perform 3 way partition where we have 4 components of the array - region w 'R', region w 'G', in-progress region, region w 'B'.

initalise 3 pointers - start (start of 'R' region), current (start of in progress region), high(start of 'B' region).


"""
PIVOT = 2

class Solution:
        def sortColors(self, nums: List[int]) -> None:
                
                mappings = {'R' : 1, 'G' : 2, 'B' : 3}
                
                n = len(nums)
                if n == 1:
                        return nums
                
                low = 0
                high = n-1
                current = 1
                
                while current <= high:
                        if mappings[nums[current]] < PIVOT:
                                nums[current], nums[low] = nums[low], nums[current]
                                low += 1
                        
                        elif mappings[nums[current]] > PIVOT:
                                nums[current], nums[high] = nums[high], nums[current]
                                high -= 1
                        
                        else:
                                current += 1

sol = Solution()
nums = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
sol.sortColors(nums)
print(nums)
                