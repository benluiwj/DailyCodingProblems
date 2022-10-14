# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given a string which we can delete at most k, return whether you can make a
# palindrome.

# For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get
# 'waterretaw'.

"""

recursively if the two letters are the same, we continue inwards
if they are different, either delete the front or delete the back
if k == 0 and the string is not a palindrome then we return false

find longest palindromic subsequence and then subtract from the length to see if it falls less than k

"""

def make_palindrome(s, k):
        n = len(s)
        # if s is a single character, its a palindrome, return true
        if n == 1:
                return True
        
        # if k is zero, means that we use all our deletions so we check if s is a palindrome
        if k == 0:
                return s == s[::-1]
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
                dp[i][i] = 1
                
        for i in range(n-2, -1, -1):
                for j in range(i+1, n):
                        if s[i] == s[j]:
                                dp[i][j] = 2 + dp[i+1][j-1]
                        else:
                                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        
        
        return n - dp[0][-1] < k

make_palindrome( 'waterrfetawx', 2)
        
        
        
        
        # # if the first and last is the same, go inwards
        # if s[0] == s[-1]:
        #         return make_palindrome(s[1:-1], k)
        
        # # try deleting either the start character or the end character
        # return make_palindrome(s[1:], k-1) or make_palindrome(s[:-1], k-1)
