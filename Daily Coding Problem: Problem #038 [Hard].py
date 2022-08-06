# Good morning! Here's your coding interview problem for today.

# This problem was asked by Microsoft.

# You have an N by N board. Write a function that, given N, returns the number of
# possible arrangements of the board where N queens can be placed on the board
# without threatening each other, i.e. no two queens share the same row, column,
# or diagonal.

from typing import *

def does_threaten(try_coord, coords):
        # check vertical
        row, col = try_coord
        
        for coord_x, coord_y in coords:
                if coord_y == col:
                        return True
                
                if abs(coord_y - col) == abs(coord_x - row):
                        return True
        
        return False
                
                

class Solution:
        def totalNQueens(self, n: int) -> int:
                def helper(n, coords):
                        if len(coords) == n:
                                return 1
                        
                        result = 0
                        start = len(coords)
                        for i in range(n):
                                try_coord = [start, i]
                                if not does_threaten(try_coord, coords):
                                        coords.append(try_coord)
                                        result += helper(n, coords)
                                        coords.pop()
                        
                        return result
                
                return helper(n, [])

sol = Solution()

ans = [1,0,0,2,10,4,40,92,352]

for i in range(9):
        actual = sol.totalNQueens(i+1)
        assert actual == ans[i]
        print('Correct for n = ' + str(i))