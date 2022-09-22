# Good morning! Here's your coding interview problem for today.

# This problem was asked by Microsoft.

# Given an array of numbers, find the length of the longest increasing subsequence
# in the array. The subsequence does not necessarily have to be contiguous.

# For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7,
# 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
from typing import *


"""

naively we can do DFS from every node to every other node, maintaining that it is increasing

greedily take the shortest may not always work

this means dp must prolly be used.

at our current position, try look back and see if there are values that are smaller.

if they are we take the longest and add 1



"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = [1 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            current = result[i]
            for j in range(i):
                if nums[j] < nums[i]:
                    current = max(current, result[i] + result[j])
            
            result[i] = current
        
        return max(result)

sol = Solution()

sol.lengthOfLIS([10,9,2,5,3,7,101,18])