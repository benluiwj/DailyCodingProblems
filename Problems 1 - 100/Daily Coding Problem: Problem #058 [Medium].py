# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# An sorted array of integers was rotated an unknown number of times.

# Given such an array, find the index of the element in the array in faster than
# linear time. If the element doesn't exist in the array, return null.

# For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4
# (the index of 8 in the array).

# You can assume all the integers in the array are unique.
"""

find the true start and how far it is from index 0 (find the valley)
when doing binary search, check the true position of the number for searching the array

[4,5,6,7,0,1,2]
         0 1 2 3 4 5 6 7

"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        start = 0
        end = n - 1
        right_pt = nums[-1]
        
        true_start = -1
        
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] < nums[(mid + 1) % n] and nums[mid] < nums[(mid - 1) % n]:
                true_start = mid
                break
            
            if nums[mid] < right_pt:
                end = mid
            
            else:
                start = mid + 1
        
        print(true_start)
        
        start = true_start
        end = true_start + n - 1
        
        while start < end:
            mid = start + (end - start) // 2
            if target <= nums[mid % n]:
                end = mid
            
            else:
                start = mid + 1
        
        return start % n if nums[start % n] == target else -1
        


sol = Solution()

"""
           v
[5 7 1 2 3 5 7]
             ^
         ^
"""

print(sol.search([5,1,2,3], 2))
        