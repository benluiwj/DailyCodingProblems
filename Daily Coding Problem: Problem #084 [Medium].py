# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1
# represents land and 0 represents water, so an island is a group of 1s that are
# neighboring whose perimeter is surrounded by water.

# For example, this matrix has 4 islands.

# 1 0 0 0 0
# 0 0 1 1 0
# 0 1 1 0 0
# 0 0 0 0 0
# 1 1 0 0 1
# 1 1 0 0 1

from typing import *

UP = [0, -1]
DOWN = [0,1]
LEFT = [-1, 0]
RIGHT = [1,0]

DIRECTIONS = [UP, DOWN, LEFT, RIGHT]
LAND = "1"

def is_valid(x,y,m,n):
        return 0 <= x < m and 0 <= y < n

class Solution:
        def numIslands(self, grid):
                m = len(grid)
                n = len(grid[0])
                visited = [[False for _ in range(n)] for _ in range(m)]
                
                count = 0
                
                for row in range(m):
                        for col in range(n):
                                if not visited[row][col] and grid[row][col] == LAND:
                                        frontier = [[row, col]]
                                        visited[row][col] = True
                                        while frontier:
                                                new_frontier = []
                                                for x,y in frontier:
                                                        for d_x, d_y in DIRECTIONS:
                                                                new_x = x + d_x
                                                                new_y = y + d_y
                                                                if is_valid(new_x, new_y, m, n) and not visited[new_x][new_y] and grid[new_x][new_y] == LAND:
                                                                        new_frontier.append([new_x, new_y])
                                                                        visited[new_x][new_y] = True
                                                
                                                frontier = new_frontier
                                        
                                        count += 1
                
                return count
        
sol = Solution()

sol.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])