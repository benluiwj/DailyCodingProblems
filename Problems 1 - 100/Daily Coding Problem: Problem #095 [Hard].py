# Good morning! Here's your coding interview problem for today.

# This problem was asked by Palantir.

# Given a number represented by a list of digits, find the next greater
# permutation of a number, in terms of lexicographic ordering. If there is not
# greater permutation possible, return the permutation with the lowest
# value/ordering.

# For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should
# return [2,1,3]. The list [3,2,1] should return [1,2,3].

# Can you perform the operation without allocating extra memory (disregarding the
# input memory)?

from typing import *

"""

naively - generate all permutations and see the next one

the permutations are always increasing, only wrapping around when its the biggest possible.

wraps around when its decreasing => reverse the entire list

[3 2 1] -> [1 2 3]

using this idea the next permutation will prolly be reversed of the subarray, checking for when it first decreases

[1 3 2] -> [2 1 3]

find the peak linearly, in this case its 3. if the list is strictly decreasing, swap the first and last, flip everything

how to know where we are in the permutation?

[1 2 3] [1 3 2]
[2 1 3] [2 3 1]
[3 1 2] [3 2 1]

if its increasing => start of sequence => flip last 2
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        