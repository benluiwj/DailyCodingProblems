# Good morning! Here's your coding interview problem for today.

# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at index i 
# of the new array is the product of all the numbers in the original array except
# the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be 
# [2, 3, 6].

# Follow-up: what if you can't use division?
def product_except_self(nums):
        # n = len(nums)
        # forward = [1 for _ in range(n)]

        # for i in range(1, n):
        #         forward[i] = forward[i-1] * nums[i-1]
        
        # backward = [1 for _ in range(n)]
        # for i in range(n-2, -1, -1):
        #         backward[i] = backward[i+1] * nums[i+1]
        
        # result = []
        # for i in range(n):
        #         result.append(backward[i] * forward[i])
        
        # return result
        n = len(nums)
        result = [1 for _ in range(n)]
        for i in range(1, n):
                result[i] = result[i-1] * nums[i-1]
        
        backward = 1
        for i in range(n-2, -1, -1):
                result[i] *= backward * nums[i+1]
                backward = backward * nums[i+1] 
        
        return result

# Time: O(n), Space: O(1) where n is length of array

assert product_except_self([1,2,3,4,5]) == [120, 60, 40, 30, 24]
assert product_except_self([3,2,1]) == [2,3,6]