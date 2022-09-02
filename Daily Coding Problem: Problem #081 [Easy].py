# Good morning! Here's your coding interview problem for today.

# This problem was asked by Yelp.

# Given a mapping of digits to letters (as in a phone number), and a digit string,
# return all possible letters the number could represent. You can assume each
# valid number in the mapping is a single digit.

# For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should
# return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].

from typing import *

NUMBERS = {"2" : ["a", "b", "c"],
           "3" : ["d", "e", "f"],
           "4" : ["g", "h", "i"],
           "5" : ["j", "k", "l"],
           "6" : ["m", "n", "o"],
           "7" : ["p", "q", "r", "s"],
           "8" : ["t", "u", "v"],
           "9" : ["w", "x", "y", "z"]
           }


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        def helper(curr, index):
            if len(curr) == len(digits):
                result.append(curr[::])
                return
            
            letters = NUMBERS[digits[index]]
            
            for char in letters:
                temp = curr + char
                helper(temp, index + 1)
        
        if not digits:
            return result
        
        first = NUMBERS[digits[0]]
        for char in first:
            curr = char
            helper(curr, 1)
        
        return result
    
sol = Solution()

sol.letterCombinations("23")
            
        
        