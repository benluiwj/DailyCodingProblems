# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# A knight's tour is a sequence of moves by a knight on a chessboard such that all
# squares are visited once.

# Given N, write a function to return the number of knight's tours on an N by N
# chessboard.

UP_AND_LEFT = [2, -1]
UP_AND_RIGHT = [2, 1]
LEFT_AND_UP = [1, -2]
LEFT_AND_DOWN = [1, 2]
DOWN_AND_LEFT = [-2, -1]
DOWN_AND_RIGHT = [-2, 1]
RIGHT_AND_UP = [1, 2]
RIGHT_AND_DOWN = [-1, 2]

MOVES = [UP_AND_LEFT, UP_AND_RIGHT, LEFT_AND_DOWN, LEFT_AND_UP, DOWN_AND_LEFT, DOWN_AND_RIGHT, RIGHT_AND_DOWN, RIGHT_AND_UP]

"""

use backtracking and increase the count accordingly.

"""

def is_valid(x ,y , n):
        return 0 <= x < n and 0 <= y < n 

def knight_tour(n):
        visited = set()
        total_pts = n * n
        count = [0]
        
        def helper(current_x, current_y):
                if len(visited) == total_pts:
                        count[0] += 1
                        return 
                
                for move in MOVES:
                        new_x = current_x + move[0]
                        new_y = current_y + move[1]
                        
                        if is_valid(new_x, new_y, n):
                                coord = (new_x,new_y)
                                visited.add(coord)
                                helper(new_x, new_y)
                                visited.remove(coord)
        
        for i in range(n):
                for j in range(n):
                        helper(i, j)
        
        return count[0]