# Good morning! Here's your coding interview problem for today.

# This problem was asked by Slack.

# You are given an N by M matrix of 0s and 1s. Starting from the top left corner,
# how many ways are there to reach the bottom right corner?

# You can only move right and down. 0 represents an empty space while 1 represents
# a wall you cannot walk through.

# For example, given the following matrix:

# [[0, 0, 1],
#  [0, 0, 1],
#  [1, 0, 0]]


# Return two, as there are only two ways to get to the bottom right:

#  * Right, down, down, right
#  * Down, right, down, right

# The top left corner and bottom right corner will always be 0.

from typing import *

"""

naively -> run bfs and increase count when we reach the last cell.

create a matrix that counts the number of ways.

simple problem: how many ways from top to bottom assume no obstacles (ie whole board is 0)

since only can go down and right, initialise first row to all 1s and first col to all 1s.

beginning at second col, take from top and left

if current step is obstacle take as 0

"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        
        for i in range(cols):
            if not obstacleGrid[0][i]:
                dp[0][i] = 1
            
            else:
                break
        
        for i in range(rows):
            if not obstacleGrid[i][0]:
                dp[i][0] = 1
            
            else:
                break
        
        for row in range(1 , rows):
            for col in range(1, cols):
                if not obstacleGrid[row][col]:
                    dp[row][col] = dp[row-1][col] + dp[row][col-1]
        
        return dp[-1][-1]

