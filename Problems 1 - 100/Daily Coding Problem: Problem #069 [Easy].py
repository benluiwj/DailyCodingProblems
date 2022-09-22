# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given a list of integers, return the largest product that can be made by
# multiplying any three integers.

# For example, if the list is [-10, -10, 5, 2], we should return 500, since that's 
# -10 * -10 * 5.

# You can assume the list has at least three integers.

from typing import *

"""

naively, go through the array 3 times to get the product.

must contain the biggest number naturally.

cannot go biggest to smallest because of negative numbers

take out biggest,
take the two smallest and multiply them
take the second two biggest and multiply them

compare, take the bigger result and multiply with the biggest number
runs in O(n log n) because of sorting

alternatively, finding manually by initialising 5 variables will run in linear time.
5 vars - max1, max2, max3, min1, min2

if num > max1:
    max1 = num
    assign current values of max1, max2 to the one behind

elif num > max2:
    max2 = num
    assign current value of max2 to max3

elif num > max3:
    max3 = num

if num < min1:
    min1 = num
    assign current value of min1 to min2

elif num < min2:
    min2 = num
"""


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2]*nums[-3])
