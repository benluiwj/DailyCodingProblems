# Good morning! Here's your coding interview problem for today.

# This problem was asked by Airbnb.

# Given a list of integers, write a function that returns the largest sum of
# non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1,
# 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?

def largest_non_adjacent_sum(nums):
        if not nums:
                return 0
        
        biggest = max(nums[-1], 0)
        second_biggest = max(nums[-2], nums[-1], 0)
        n = len(nums)
        for i in range(n - 3, -1, -1):
                current = max(nums[i] + biggest, second_biggest, 0)
                biggest = second_biggest
                second_biggest = current
                
        
        return max(biggest, second_biggest)
        
        
        # if not nums:
        #         return 0
        
        # n = len(nums)
        # dp = [[0 for _ in range(n)] for _ in range(n)]
        
        # for i in range(n):
        #         dp[i][i] = nums[i]
        
        # for i in range(n-1):
        #         dp[i][i+1] = max(nums[i], nums[i+1])
                
        # for row in range(n-2, -1, -1):
        #         for col in range(row+2, n):
        #                 dp[row][col] = max(nums[row] + dp[row+2][col], dp[row+1][col])
        
        # return dp[0][-1]
        # if not nums:
        #         return 0
        # if len(nums) == 1:
        #         return nums[0]
        
        # if len(nums) == 2:
        #         return max(nums[0], nums[1])
        
        # return max(nums[0] + largest_non_adjacent_sum(nums[2:]), largest_non_adjacent_sum(nums[1:]))

assert largest_non_adjacent_sum([2,4,6,2,5]) == 13
assert largest_non_adjacent_sum([5,1,-1,-5]) == 5