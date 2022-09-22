# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given a list of integers S and a target number k, write a function that returns
# a subset of S that adds up to k. If such a subset cannot be made, then return
# null.

# Integers can appear more than once in the list. You may assume all numbers in
# the list are positive.

# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1]
# since it sums up to 24.

"""

find every subset -> find subset that sums to k -> O(2^ n) for subsets * O(n) for checking sum

to do better -> use backtracking and stop when the sum equals to k.

O(n^2) check every element * O(n) check sum


Construct a table A that's size len(nums) + 1 by k + 1. At each index A[i][j], we'll keep a subset of the list from 0..i (including lower, excluding upper bound) that can add up to j, or null if no list can be made. Then we will fill up the table using pre-computed values and once we're done, we should be able to just return the value at A[-1][-1]. 
"""

def subset_sum_to_k(nums, k):
        # At each index A[i][j], we'll keep a subset of the list from 0..i (including lower, excluding upper bound) that can add up to j, or null if no list can be made. 
        
        
        n = len(nums)
        A = [[None for _ in range(k + 1)] for _ in range(n + 1)]
        
        # initialize each element of the first row (A[i][0] for i in range(len(nums) + 1)) with the empty list, since any subset of the list can make 0
        for i in range(n + 1):
                A[i][0] = []
        
        for i in range(1, n + 1):
                for j in range(1, k + 1):
                        last = nums[i - 1]
                        if last > j:
                                A[i][j] = A[i - 1][j]
                        
                        else:
                                if A[i - 1][j] is not None:
                                        A[i][j] = A[i - 1][j]
                                
                                elif A[i - 1][j - last] is not None:
                                        A[i][j] = A[i - 1][j - last] + [last]
                                        
                                else:
                                        A[i][j] = None
        
        return A[-1][-1]

subset_sum_to_k([12, 1, 61, 5, 9, 2], 24)
                        