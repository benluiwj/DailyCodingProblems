# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# The edit distance between two strings refers to the minimum number of character
# insertions, deletions, and substitutions required to change one string to the
# other. For example, the edit distance between “kitten” and “sitting” is three:
# substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

# Given two strings, compute the edit distance between them.
from typing import *

"""

if both words are blank -> return 0

if either word is blank -> return length of the other since we insert every letter into it

if the first characters are the same -> dont do anything and go to the next one

otherwise, try either inserting(assume insert into first place for word1), delete(assume delete first char for word1), edit(assume edit first char to correct, continue to next)

perform the same action but in a table -> word1(col) by word2(row)
diagonal is edit, column traversal is delete, horizontal is insert

"""

class Solution:
        def minDistance(self, word1: str, word2: str) -> int:
                m = len(word1)
                n = len(word2)
                
                dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
                
                for i in range(m+1):
                        dp[i][0] = i
                
                for j in range(n+1):
                        dp[0][j] = j
                
                for i in range(1, m + 1):
                        for j in range(1, n + 1):
                                if word1[i-1] == word2[j - 1]:
                                        dp[i][j] = dp[i-1][j-1]
                                
                                else:
                                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                
                return dp[-1][-1]
                
                # if word1[0] == word2[0]:
                #         return self.minDistance(word1[1:], word2[1:])
                
                # insert = 1 + self.minDistance(word1, word2[1:])
                # delete = 1 + self.minDistance(word1[1:], word2)
                # edit = 1 + self.minDistance(word1[1:], word2[1:])
                
                # return min(insert, delete, edit)
        
                
                