# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

# For example, given the following matrix:

# [[1,  2,  3,  4,  5],
#  [6,  7,  8,  9,  10],
#  [11, 12, 13, 14, 15],
#  [16, 17, 18, 19, 20]]


# You should print out the following:

# 1
# 2
# 3
# 4
# 5
# 10
# 15
# 20
# 19
# 18
# 17
# 16
# 11
# 6
# 7
# 8
# 9
# 14
# 13
# 12

from typing import *

"""

right -> down -> left -> up

right: (0,0) -> (1, 0) ... (n, 0)
down: (n,0) -> (n, 1) ... (n,m)
left: (n,m) -> (n-1,m)... (0,m)
up: (0,m) -> (0, m-1)... (0,1)

right: (0,1) -> (1,1) ... (n-1,1)
down: (n,1) -> (n,2) ... (n, m-1)
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        count = 0
        m = len(matrix)
        n = len(matrix[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        while len(result) < m * n:
                # go right
                for i in range(count, n - count):
                        if not visited[count][i]:
                                visited[count][i] = True
                                result.append(matrix[count][i])
                
                # go down
                for i in range(count+1, m - count):
                        if not visited[i][n-count-1]:
                                visited[i][n-count-1] = True
                                result.append(matrix[i][n-count-1])
                
                # go left
                for i in range(n-count-2, count, -1):
                        if not visited[m-count-1][i]:
                                visited[m-count-1][i] = True
                                result.append(matrix[m-count-1][i])
                
                # go up
                for i in range(m-count-1, count, -1):
                        if not visited[i][count]:
                                visited[i][count] = True
                                result.append(matrix[i][count])
                
                count += 1
        
        return result

sol = Solution()

assert sol.spiralOrder([[3],[2]]) == [3,2]
assert sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]

assert sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]