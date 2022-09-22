# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given an N by N matrix, rotate it by 90 degrees clockwise.

# For example, given the following matrix:

# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]


# you should return:

# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]


# Follow-up: What if you couldn't use any extra space?

"""
rotate 90 degrees clockwise:

top edge become right
right edge become bottom
bottom edge become left
left edge become top

with extra space:
1) create new matrix
2) perform swaps to fulfill the condition above
3) reallocate the matrix above

without extra space, perform swap simulateneuously

for 3 by 3, go through 0 row
for 4 by 4, go through 0 row then go through 1 row starting from 1 index
for 5 by 5, go through 0 row, go through 1 starting from 1, go through 2nd starting from 2


"""

from typing import *

class Solution:
        def rotate(self, matrix: List[List[int]]) -> None:
                n = len(matrix)
                
                for i in range(n):
                        for j in range(i, n - 1 -i):
                                # top, right, bottom, left = left, top, right, bottom
                                # top = matrix[i][j]
                                # right = matrix[j][n-1-i]
                                # bottom = matrix[n-1-i][n - 1 - j]
                                # left = matrix[n - 1 - j][i]
                                
                                matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n - 1 - j], matrix[n - 1 - j][i] = matrix[n - 1 - j][i], matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n - 1 - j]
                                
                
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# matrix3 = [[4,8], [3,6]]

sol = Solution()


# sol.rotate(matrix3)
sol.rotate(matrix1)

assert matrix1 == [[7,4,1],[8,5,2],[9,6,3]]

sol.rotate(matrix2)

assert matrix2 == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]