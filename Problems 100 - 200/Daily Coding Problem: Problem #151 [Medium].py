# Good morning! Here's your coding interview problem for today.

# Given a 2-D matrix representing an image, a location of a pixel in the screen
# and a color C, replace the color of the given pixel and all adjacent same
# colored pixels with C.

# For example, given the following matrix, and location pixel of (2, 2), and 'G'
# for green:

# B B W
# W W W
# W W W
# B B B


# Becomes

# B B G
# G G G
# G G G
# B B B

"""

find previous color that we want to change

change the color at the specified location

perform bfs on the surroundings and change the colors if they are the same as the previous color


"""


UP = [0, -1]
DOWN = [0, 1]
LEFT = [-1, 0]
RIGHT = [1, 0]

DIRECTIONS = [UP, DOWN,LEFT,RIGHT]


def replacePixel(matrix, location, color):
        curr_color = matrix[location[0]][location[1]]
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        frontier = set(location)
        
        while frontier:
                new_frontier = set()
                for x, y in frontier:
                        matrix[y][x] = color
                        for direction in DIRECTIONS:
                                new_x = x + direction[0]
                                new_y = y + direction[1]
                                
                                if 0 <= new_x < cols and 0 <= new_y < rows:
                                        if matrix[new_y][new_x] == curr_color:
                                                new_frontier.add([new_x, new_y])
                                                matrix[new_y][new_x] = color
                
                frontier = new_frontier
                                                