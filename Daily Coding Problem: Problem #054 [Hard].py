# Good morning! Here's your coding interview problem for today.

# This problem was asked by Dropbox.

# Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with
# digits. The objective is to fill the grid with the constraint that every row,
# column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

# Implement an efficient sudoku solver.

from typing import *

"""

use dfs to fill the cells, checking whether the fill is valid or not by checking the columns and rows and the box it is in.

"""
BLANK = "."
NUMBERS = {"1", "2", "3", "4", "5", "6","7", "8", "9"}

def is_solved(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == BLANK:
                return False
    
    return True

def is_valid(board):
    return valid_cols(board) and valid_boxes(board) and valid_rows(board)

def valid_cols(board):
    for i in range(9):
        column = set()
        for col in range(9):
            if board[i][col] != BLANK and board[i][col] not in column:
                column.add(board[i][col])
            
            else:
                return False
    
    return True

def valid_rows(board):
    for i in range(9):
        row = set()
        for j in range(9):
            if board[i][j] != BLANK and board[i][j] not in row:
                row.add(board[i][j])
            
            else:
                return False
    
    return True

def valid_boxes(board):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box = set()
            for n in range(3):
                for m in range(3):
                    if board[i+n][j+m] != BLANK and board[i][j] not in box:
                        box.add(board[i+n][j+m])
                    else:
                        return False
    
    return True

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if is_solved(board):
            return
        
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == BLANK:
                    for k in range(1, 10):
                        if is_valid(k, i,j, board):
                            board[i][j] = str(k)
                            self.solveSudoku(board)
                            if is_solved(board):
                                return
                            
                            
        