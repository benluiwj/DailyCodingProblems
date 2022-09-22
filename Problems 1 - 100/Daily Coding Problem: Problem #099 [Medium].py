# Good morning! Here's your coding interview problem for today.

# This problem was asked by Microsoft.

# Given an unsorted array of integers, find the length of the longest consecutive
# elements sequence.

# For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element
# sequence is [1, 2, 3, 4]. Return its length: 4.

# Your algorithm should run in O(n) complexity.

def consecutive_elements(nums):
        set_nums = set(nums)
        
        result = 0
        for num in nums:
                if num - 1 not in set_nums:
                        length = 1
                        temp = num
                        while temp in set_nums:
                                temp += 1
                                length += 1
                        
                        result = max(result, length)
        
        return result