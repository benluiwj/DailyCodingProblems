# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given a array of numbers representing the stock prices of a company in
# chronological order, write a function that calculates the maximum profit you
# could have made from buying and selling that stock once. You must buy before you
# can sell it.

# For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could
# buy the stock at 5 dollars and sell it at 10 dollars.

from typing import *

"""

do it naively - buying is a subtraction, selling is addition. compare with every other and see the max.

to get most profit - buy low sell high

an array that contains the biggest values from future till now

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        biggest = [0 for _ in range(n)]
        biggest[-1] = prices[-1]
        for i in range(n - 2, -1, -1):
            biggest[i] = max(biggest[i+1], prices[i])
        
        print(biggest)
        profit = 0
        
        for i, price in enumerate(prices):
            profit = max(profit, biggest[i] - price)
        
        return profit
    
sol = Solution()

sol.maxProfit([7,1,5,3,6,4])
    
