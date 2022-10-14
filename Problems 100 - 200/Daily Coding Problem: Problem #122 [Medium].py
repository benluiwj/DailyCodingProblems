# Good morning! Here's your coding interview problem for today.

# This question was asked by Zillow.

# You are given a 2-d matrix where each cell represents number of coins in that
# cell. Assuming we start at matrix[0][0], and can only move right or down, find
# the maximum number of coins you can collect by the bottom right corner.

# For example, in this matrix

# 0 3 1 1
# 2 0 0 4
# 1 5 3 1


# The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.

def collect_max(matrix):
        collection = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        collection[0][0] = matrix[0][0]
        
        for i in range(1, len(matrix[0])):
                collection[0][i] = matrix[0][i] + collection[0][i-1]
        
        for j in range(1, len(matrix)):
                collection[j][0] = matrix[j][0] + collection[j-1][0]
                
        
        for i in range(1, len(matrix)):
                for j in range(1, len(matrix[0])):
                        collection[i][j] = matrix[i][j] + max(collection[i-1][j], collection[i][j-1])
        
        return collection[-1][-1]

matrix = [[0,3,1,1], [2,0,0,4], [1,5,3,1]]
collect_max(matrix)