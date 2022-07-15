# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# You are given an M by N matrix consisting of booleans that represents a board.
# Each True boolean represents a wall. Each False boolean represents a tile you
# can walk on.

# Given this matrix, a start coordinate, and an end coordinate, return the minimum
# number of steps required to reach the end coordinate from the start. If there is
# no possible path, then return null. You can move up, left, down, and right. You
# cannot move through walls. You cannot wrap around the edges of the board.

# For example, given the following board:

# [[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]


# and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number
# of steps required to reach the end is 7, since we would need to go through (1,
# 2) because there is a wall everywhere else on the second row.

UP = [0, -1]
DOWN = [0, 1]
LEFT = [-1, 0]
RIGHT = [1, 0]

DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

def is_valid(new_x, new_y, m, n):
        return 0 <= new_x < m and 0 <= new_y < n

def min_steps(start, end, board):
        n = len(board)
        m = len(board[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        
        frontier = set()
        frontier.add(start)
        count = 0
        while frontier:
                new_frontier = set()
                for point in frontier:
                        x , y = point
                        if x == end[0] and y == end[1]:
                                return count 
                        visited[x][y] = True
                        for direction in DIRECTIONS:
                                new_x = x + direction[0]
                                new_y = y + direction[1]
                                
                                if is_valid(new_x, new_y, m, n) and not board[new_x][new_y]:
                                        new_frontier.add((new_x, new_y))
                count += 1
                frontier = new_frontier
        
        return None



board = [[False, False, False, False],
[True, True, False, True],
[False, False, False, False],
[False, False, False, False]]

print(min_steps((3,0), (0,0), board))