# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given a start word, an end word, and a dictionary of valid words, find the
# shortest transformation sequence from start to end such that only one letter is
# changed at each step of the sequence, and each transformed word exists in the
# dictionary. If there is no possible transformation, return null. Each word in
# the dictionary have the same length as start and end and is lowercase.

# For example, given start = "dog", end = "cat", and dictionary = {"dot", "dop",
# "dat", "cat"}, return ["dog", "dot", "dat", "cat"].

# Given start = "dog", end = "cat", and dictionary = {"dot", "tod", "dat", "dar"},
# return null as there is no possible transformation from dog to cat.
from typing import *
import string
"""

perform dfs, collect all the transformations and return the list containing the shortest?

"""
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        dictionary = set(wordList)
        if endWord not in dictionary:
            return []
        
        visited = set()
        shortest = [float('inf')]
        lowercase = string.ascii_lowercase
        
        paths = dict()
        paths[float('inf')] = []
        
        def helper(current_ladder):
            n = len(current_ladder)
            m = len(beginWord)
            if current_ladder[-1] == endWord and n<= shortest[0]:
                if n not in paths:
                    paths[n] = [current_ladder[::]]
                else:
                    paths[n].append(current_ladder[::])
                
                shortest[0] = min(shortest[0], n)
                return
            
            last_word = current_ladder[-1]
            for i in range(m):
                prefix = last_word[:i]
                suffix = last_word[i+1:]
                for char in lowercase:
                    new_word = prefix + char + suffix
                    if new_word in dictionary  and new_word not in visited:
                        current_ladder.append(new_word)
                        visited.add(new_word)
                        helper(current_ladder)
                        current_ladder.pop()
                        visited.remove(new_word)
            
            return
                
        
        helper([beginWord])
        return paths[shortest[0]]
            

sol = Solution()

sol.findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"])
                        
                        
                