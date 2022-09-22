# Good morning! Here's your coding interview problem for today.

# This problem was asked by Coursera.

# Given a 2D board of characters and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.

# For example, given the following board:

# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]


# exists(board, "ABCCED") returns true,exists(board, "SEE") returns true,
# exists(board, "ABCB") returns false.

"""

perform dfs to check if it exists. only call dfs when the first letter matches.

"""

UP = [0, -1]
DOWN = [0, 1]
LEFT = [-1, 0]
RIGHT = [1, 0]

DIRECTIONS = [UP, DOWN,LEFT,RIGHT]



from typing import *


def is_valid(x,y,board):
    return 0 <= x < len(board[0]) and 0 <= y < len(board)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        y = len(board)
        x = len(board[0])
        
        def helper(board, visited, found, row, col):
            if found == word:
                return True
            
            if len(found) == len(word):
                return False
            
            next_char = word[len(found)]
            for x , y in DIRECTIONS:
                new_x = col + x
                new_y = row + y
                
                if is_valid(new_x, new_y, board) and not visited[new_y][new_x] and board[new_y][new_x] == next_char:
                    visited[new_y][new_x] = True
                    new_found = found + next_char
                    result = helper(board, visited, new_found, new_y, new_x)
                    if result:
                        return True
            
            return False
        
        for row in range(y):
            for col in range(x):
                if board[row][col] == word[0]:
                    visited = [[False for _ in range(x)] for _ in range(y)]
                    visited[row][col] = True
                    result = helper(board, visited, word[0], row, col)
                    if result:
                        return True
        
        return False
    
sol = Solution()

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

assert sol.exist(board, "SEE") == True