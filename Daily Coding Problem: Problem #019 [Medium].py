# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# A builder is looking to build a row of N houses that can be of K different
# colors. He has a goal of minimizing cost while ensuring that no two neighboring
# houses are of the same color.

# Given an N by K matrix where the nth row and kth column represents the cost to
# build the nthhouse with kth color, return the minimum cost which achieves this
# goal.

# Follow up: Can you solve it in O(nk) time?

def minCost(matrix):
        n = len(matrix)
        k = len(matrix[0])
        
        smallest = min(matrix[0])
        smallestIndex = -1
        secondSmallest = float('inf')
        
        for i in range(k):
                if matrix[0][i] == smallest:
                        smallestIndex = i
                
                if matrix[0][i] != smallest and matrix[0][i] < secondSmallest:
                        secondSmallest = matrix[0][i]
        
        dp = [matrix[0][i] for i in range(k)]
        
        for hse in range(1, n):
                nextSmallest = float('inf')
                nextSmallestIndex = -1
                nextSecondSmallest = float('inf')
                for col in range(k):
                        if matrix[hse][col] < nextSmallest:
                                nextSmallest = matrix[hse][col]
                                nextSmallestIndex = col
                        
                        elif matrix[hse][col] < nextSecondSmallest and nextSecondSmallest != nextSmallest:
                                nextSecondSmallest = matrix[hse][col]
                        
                        if col == smallestIndex:
                                dp[col] = matrix[hse][col] + secondSmallest
                        
                        else:
                                dp[col] = matrix[hse][col] + smallest
                        
                smallest = nextSmallest
                smallestIndex = nextSmallestIndex
                secondSmallest = nextSecondSmallest
        
        return min(dp)
        
        
        # dp = [[float('inf') for _ in range(k)] for _ in range(n)]
        
        # for col in range(k):
        #         dp[0][col] = matrix[0][col]
        
        # for hse in range(1, n):
        #         for col in range(k):
        #                 for i in range(k):
        #                         if i != col:
        #                                 dp[hse][col] = min(matrix[hse][col] + dp[hse-1][i], dp[hse][col])
                                        
        # Time : O(nk^2), Space : O(nk)         
        # return min(dp[-1])

print(minCost([[1,5,3],[2,9,4]]))
        