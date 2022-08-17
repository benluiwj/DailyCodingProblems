# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Given an array of numbers, find the maximum sum of any contiguous subarray of
# the array.

# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be
# 137, since we would take elements 42, 14, -5, and 86.

# Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not
# take any elements.

# Do this in O(N) time.

from typing import *

"""

naively: look at every contiguous subarray and take the one with the maximum - O(n^2)

[5,4,-1,7,8]

[5] [5 4] [5 4 -1] [5 4 -1 7] [5 4 -1 7 8]
    [4] [4 -1] [4 -1 7] [4 -1 7 8]
        [-1] [-1 7] [-1 7 8]
             [7] [7 8]
                 [8]   

[-2,1,-3,4,-1,2,1,-5,4]


https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d
Loop invariant: in jth step, max_so_far holds maximum of sum A[0]...A[j-1]. To include A[j], use max_ending_here
= max(max_ending_here, A[j] + max_ending_here). max_so_far just take the larger of the 2.
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
            max_so_far = 0
            max_ending_here = 0
            
            for num in nums:
                max_ending_here = max(max_ending_here, num + max_ending_here)
                max_so_far = max(max_so_far, max_ending_here)
            
            return max_so_far
            

sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))



        