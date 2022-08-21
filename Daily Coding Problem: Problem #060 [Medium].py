# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given a multiset of integers, return whether it can be partitioned into two
# subsets whose sums are the same.

# For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return
# true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both
# add up to 55.

# Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't
# split it up into two subsets that add up to the same sum.
"""

if the sum of array is divisible by 2, we know it can be partitioned
then we try to include elements into an array such that it sums up accordingly.

create a dp array that has the elements as columns and the values of the target from 1 to target.
returning the value at the bottom right corner of the dp.

if there are n elements, let the target value be m

then the resulting time complexity would be O(mn)

"""


from typing import *

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        if total % 2:
            return False
        
        target = total // 2
        
        dp = [[False for _ in range(n+1)] for _ in range(target+1)]
        
        for j in range(n+1):
                dp[0][j] = True
                
        for i in range(1, target+1):
                for j in range(1, n+1):
                        last = i - nums[j-1]
                        if last >= 0:
                                dp[i][j] = dp[i][j-1] or dp[last][j-1]
                        
                        else:
                                dp[i][j] = dp[i][j-1]
        
        return dp[-1][-1]

sol = Solution()
assert sol.canPartition([1,2,5]) == False
assert sol.canPartition([1,2,3,5]) == False
assert sol.canPartition([15, 5, 20, 10, 35, 15, 10]) == True
        