# Good morning! Here's your coding interview problem for today.

# This problem was asked by MongoDB.

# Given a list of elements, find the majority element, which appears more than
# half the time (> floor(len(lst) / 2.0)).

# You can assume that such element exists.

# For example, given [1, 2, 1, 1, 3, 4, 0], return 1.

from typing import *

"""

create a table that counts the frequency
once the frequency is reached return the key 
runs in O(n) time and O(n) space

FOLLOW UP: Solve in constant space

Use a voting algorithm

since majority must exist, this means that its overall vote should be positive
if the overall vote <= 0, then we choose another element. 

"""

import math

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = math.floor(len(nums) // 2)
        
        table = dict()
        for num in nums:
            if num in table:
                table[num] += 1
            
            else:
                table[num] = 1
            
            if table[num] > majority:
                return num
        
        