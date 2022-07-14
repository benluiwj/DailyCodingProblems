# Good morning! Here's your coding interview problem for today.

# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the
# list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?


def twoSum(nums, k):
        seen = set()
        for num in nums:
                if k - num in seen:
                        return True
                seen.add(num)
        
        return False

# Time : O(n)
# Space : O(n)
# where n is length of array

assert twoSum([10,15,3,7], 17) == True
print('Success!')