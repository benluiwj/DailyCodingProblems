# Good morning! Here's your coding interview problem for today.

# This problem was asked by Lyft.

# Given a list of integers and a number K, return which contiguous elements of the
# list sum to K.

# For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return
# [2, 3, 4], since 2 + 3 + 4 = 9.

"""

naively, check every subarray to see whether it sums to K

sliding window to check whether the current sum is greater than window or not. if its greater than we reduce the size of the window?

"""


def subarraySum(nums, k):
        start = 0
        end = 0
        
        curr_sum = 0
        while end < len(nums):
                curr_sum += nums[end]
                
                while curr_sum > k:
                        curr_sum -= nums[start]
                        start += 1
                
                if curr_sum == k:
                        return nums[start:end+1]
                
                end += 1
        