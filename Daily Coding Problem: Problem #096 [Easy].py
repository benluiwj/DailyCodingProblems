# Good morning! Here's your coding interview problem for today.

# This problem was asked by Microsoft.

# Given a number in the form of a list of digits, return all possible
# permutations.

# For example, given [1,2,3], return 
# [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
from typing import *

"""
dfs

"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = set()
            
        def helper(curr):
                if len(curr) == len(nums):
                    return [curr[::]]
                
                cumulative = []
                
                for i in range(len(nums)):
                    if nums[i] not in visited:
                        visited.add(nums[i])
                        curr.append(nums[i])
                        cumulative.extend(helper(curr))
                        curr.pop()
                        visited.remove(nums[i])
                
                return cumulative
        
        return helper([])
    

sol = Solution()

sol.permute([1,2,3])
                
                
                    
        