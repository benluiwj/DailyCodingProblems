# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# You are given an array of length n + 1 whose elements belong to the set {1, 2,
# ..., n}. By the pigeonhole principle, there must be a duplicate. Find it in
# linear time and space.

from typing import *

"""

create an array of size n. since the elements run from 1 to n, assign the number to the correct index. if the index is filled already, then we know its the duplicate.


"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
            pigeonhole = [0 for i in range(len(nums))]
            
            for num in nums:
                    if pigeonhole[num - 1] != 0:
                            return num
                    
                    pigeonhole[num - 1] = num
        