# Good morning! Here's your coding interview problem for today.

# This problem was asked by Microsoft.

# Given a 2D matrix of characters and a target word, write a function that returns
# whether the word can be found in the matrix by going left-to-right, or
# up-to-down.

# For example, given the following matrix:

# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]


# and the target word 'FOAM', you should return true, since it's the leftmost
# column. Similarly, given the target word 'MASS', you should return true, since
# it's the last row.

def wordSearch(matrix, word):
        n = len(word)
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
                for j in range(cols):
                        is_found = True
                        for k in range(n):
                                if matrix[i+k][j] != word[k] and matrix[i][j+k] != word[k]:
                                        is_found = False
                                        break
                        
                        if is_found:
                                return is_found
        
        return False
                                