# Good morning! Here's your coding interview problem for today.

# This problem was asked by Airbnb.

# Given a list of words, find all pairs of unique indices such that the
# concatenation of the two words is a palindrome.

# For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0),
# (2, 3)].
from typing import * 

"""

Brute force approach -> concatenate every word with each other and see if its palindrome.
Time: O(mn^2) -> n (for first iter) * n (for second iter) * m (for palindrome check)

put every word into a hashtable and check their prefix and postfix. check each prefix and postfix to see if its in the table and if its palindromic.

if prefix/postfix is palindromic and reversed postfix/prefix in dictionary

suppose current word is aabc,

pre: a, rev_post = cba -> cba + aabc = cbaaabc (palindrome)
pre aa, rev_post = cb -> cb + aabc = cbaabc (palindrome)
pre aab, rev_post = c -> not possible to get palindrome
pre aabc, rev_post = "" -> not possible since pre is not palindrome



"""


class Solution:
        def palindromePairs(self, words: List[str]) -> List[List[int]]:
                table = dict()
                
                for i, word in enumerate(words):
                        table[i] = word
                
                result = []
                
                for i, word in enumerate(words):
                        for j in range(len(word)):
                                prefix, postfix = word[:j], word[j:]
                                reversed_pre, reversed_post = prefix[::-1], postfix[::-1]
                                
                                if prefix == reversed_pre and reversed_post in table:
                                        if i != table[reversed_post]:
                                                result.append([i, table[reversed_post]])
                                
                                if postfix == reversed_post and reversed_pre in table:
                                        if i != table[reversed_pre]:
                                                result.append([table[reversed_pre], i])
                
                return result
                                
                                