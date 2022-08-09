# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given an array of integers, return a new array where each element in the new
# array is the number of smaller elements to the right of that element in the
# original input array.

# For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

#  * There is 1 smaller element to the right of 3
#  * There is 1 smaller element to the right of 4
#  * There are 2 smaller elements to the right of 9
#  * There is 1 smaller element to the right of 6
#  * There are no smaller elements to the right of 1

from typing import *

"""

naively, just count the number of elements that are smaller than itself and add the count to the resulting array -> O(n^2)

[3 4 9 6 1]

sort in ascending order (n log n)

search for the current element in the input array (log n)

add index of that element to currrent array (1)

delete element from array O(n)

total n log n


"""
def binary_search(target, nums):
    n = len(nums)
    start = 0
    end = n - 1
    start_index = -1
    while start <= end:
        mid = start + (end - start) // 2
        
        if nums[mid] == target:
            start_index = mid
            end = mid - 1
        
        elif nums[mid] > target:
            end = mid - 1
        
        else:
            start = mid + 1
    
    start_index = start
    
    return start_index


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ascending_nums = sorted(nums)
        
        
        
        result = []
        
        for num in nums:
            index = binary_search(num, ascending_nums)
            ascending_nums.pop(index)
            result.append(index)
        
        return result
    

sol = Solution()

# assert sol.countSmaller([5,2,6,1]) == [2,1,1,0]
# assert sol.countSmaller([-1]) == [0]
# assert sol.countSmaller([0,0]) == [0,0]
# assert sol.countSmaller([3, 4, 9, 6, 1]) == [1, 1, 2, 1, 0]
assert sol.countSmaller([3, 2, 5, 6, 1]) == [2, 1, 1, 1, 0]
assert sol.countSmaller([1,1,1,0]) == [1,1,1,0]