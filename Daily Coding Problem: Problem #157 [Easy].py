# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Given a string, determine whether any permutation of it is a palindrome.

# For example, carrace should return true, since it can be rearranged to form 
# racecar, which is a palindrome. daily should return false, since there's no
# rearrangement that can form a palindrome.

"""

naively : form every possible permutation and see if they are palindromic or not

alternatively:

if length of s is even then it can form a palindrome if all letter counts are even
if length of s is odd, only 1 of the letter can have odd count

if the above conditions are fulfilled -> return true


"""

def palindrome_permutation(s):
        counter = dict()
        
        is_odd = len(s) % 2 == 1
        
        for char in s:
                if char in counter:
                        counter[char] += 1
                
                else:
                        counter[char] = 1
        
        odd_found = False
        
        for value in counter.values():
                if value % 2 == 1:
                        if is_odd:
                                if not odd_found:
                                        odd_found = True
                                
                                else:
                                        return False
                        
                        else:
                                return False
        
        return True

assert palindrome_permutation('carrace') == True
assert palindrome_permutation('daily') == False   
assert palindrome_permutation('aab') == True
assert palindrome_permutation('code') == False            