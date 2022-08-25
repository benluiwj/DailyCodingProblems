# Good morning! Here's your coding interview problem for today.

# This problem was asked by Dropbox.

# Given a string s and a list of words words, where each word is the same length,
# find all starting indices of substrings in sthat is a concatenation of every
# word in words exactly once.

# For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"], return
# [0, 13], since "dogcat" starts at index 0 and "catdog" starts at index 13.

# Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return [] since there
# are no substrings composed of "dog" and "cat" in s.

# The order of the indices does not matter.
from typing import * 

"""
based on the number words in words, create a sliding window that partitions at each word length. 
create a mapping of word count of words

in the sliding window partitions, see if the word permutation exists, if it does, add start index to the start
if it doesnt, shift window by length of word? or 1?
"""

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_length = len(words[0])
        substring_length = word_length * len(words)
        n = len(s)
        if substring_length > n:
                return []
        
        word_map = dict()
        for word in words:
                if word in word_map:
                        word_map[word] += 1
                else:
                        word_map[word] = 1
        
        start = 0
        end = substring_length

        result = []
        while end <= n:
                window = s[start:end]
                duplicate_map = word_map.copy()
                for i in range(0, substring_length, word_length):
                        word = window[i:i+word_length]
                        if word in duplicate_map:
                                if duplicate_map[word] > 0:
                                        duplicate_map[word] -= 1
                                
                        
                        else:
                                break
                
                if sum(duplicate_map.values()) == 0:
                        result.append(start)
                
                start += 1
                end += 1
        
        return result
        
sol = Solution()
sol.findSubstring(s = "barfoothefoobarman", words = ["foo","bar"])