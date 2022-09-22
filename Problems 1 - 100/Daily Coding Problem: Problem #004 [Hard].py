# Good morning! Here's your coding interview problem for today.

# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear
# time and constant space. In other words, find the lowest positive integer that
# does not exist in the array. The array can contain duplicates and negative
# numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should
# give 3.

# You can modify the input array in-place.
def first_missing_positive(nums):
        smallest = min(nums)
        n = len(nums)
        if smallest > 1:
                return 1
        
        
        for i in range(n):
                while i + 1 != nums[i] and 1 <= nums[i] <= n:
                        v = nums[i]
                        nums[v - 1], nums[i] = nums[i], nums[v-1]
                        if nums[v-1] == nums[i]:
                                break
        
        for i in range(1, n+1):
                if nums[i-1] != i:
                        return i
        
        return n+1
print(first_missing_positive([1,2,0]))
print(first_missing_positive([3,4,-1,1]))
print(first_missing_positive([1,1]))