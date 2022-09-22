# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the
# number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa',
# 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not
# allowed.

def numDecodings(s):
        # if s == "0" or s[0] == "0":
        #         return 0
        
        # if len(s) == 1:
        #         return 1
        
        # if len(s) == 2:
        #         if 10 <= int(s) <= 26:
        #                 return 1 + numDecodings(s[1:])
        
        # count = 0
        # two_init = s[:2]
        # if 10 <= int(two_init) <= 26:
        #         count += numDecodings(s[2:])
        
        # count += numDecodings(s[1:])
        # return count
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
                if s[i] != "0":
                        dp[i][i] = 1
        
        for row in range(n-2, -1, -1):
                if s[row] == "0" :
                        continue
                for col in range(row+1, n):
                        if col + 1 - row == 2:
                                curr = int(s[row:col+1]) 
                                if s[row] == "0":
                                        dp[row][col] = 0
                                
                                   
                                elif 10 <= curr <= 26:
                                        dp[row][col] = 1 + dp[row+1][col]
                                elif curr < 10 :
                                        dp[row][col] = 0
                                else:
                                        dp[row][col] = dp[row+1][col]
                        else:
                                if 10 <= int(s[row:row+2]) <= 26:
                                        dp[row][col] += dp[row+2][col]
                                
                                dp[row][col] += dp[row+1][col]
        
        return dp[0][-1]
        
         

print(numDecodings("30"))