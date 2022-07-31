# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# You are given an array of non-negative integers that represents a
# two-dimensional elevation map where each element is unit-width wall and the
# integer is the height. Suppose it will rain and all spots between two walls get
# filled up.

# Compute how many units of water remain trapped on the map in O(N) time and O(1)
# space.

# For example, given the input [2, 1, 2], we can hold 1 unit of water in the
# middle.

# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in
# the second, and 3 in the fourth index (we cannot hold 5 since it would run off
# to the left), so we can trap 8 units of water.
from typing import *

class Solution:
        def trap(self, height: List[int]) -> int:
                result = 0
                n = len(height)
                left_max = [0 for _ in range(n)]
                right_max = [0 for _ in range(n)]
                
                left_max[0] = height[0]
                right_max[-1] = height[-1]
                
                for i in range(1, len(height)):
                        left_max[i] = (max(height[i], left_max[i-1]))
                
                for i in range(len(height) - 2 , -1 , -1):
                        right_max[i] = (max(height[i], right_max[i+1]))
                
                
                for i in range(1 , len(height) - 1):
                        level = height[i]
                        
                        water_level = min(left_max[i-1], right_max[i+1])
                        
                        result += max(water_level - level , 0)
                
                return result
        

sol = Solution()

sol.trap([3, 0, 1, 3, 0, 5]) 