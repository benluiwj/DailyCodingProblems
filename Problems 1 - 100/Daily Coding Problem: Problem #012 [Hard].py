# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# There exists a staircase with N steps, and you can climb up either 1 or 2 steps
# at a time. Given N, write a function that returns the number of unique ways you
# can climb the staircase. The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:

#  * 1, 1, 1, 1
#  * 2, 1, 1
#  * 1, 2, 1
#  * 1, 1, 2
#  * 2, 2

# What if, instead of being able to climb 1 or 2 steps at a time, you could climb
# any number from a set of positive integers X? For example, if X = {1, 3, 5}, you
# could climb 1, 3, or 5 steps at a time.


# n = 1 -> 1
# n = 2 -> 2
# n = 3 -> 3
# n = 4 -> 5
# n = 5 -> 8
# Fibonacci sequence


def climb_steps(n):
        a = 0
        b = 1
        for _ in range(n+1):
                a, b = b, a + b
        
        return a


def better_climb_steps(n , X):
        dp = [0 for _ in range(n+1)]
        dp[0] = 0
        for i in range(1,n+1):
                cum_sum = 0
                for j in X:
                        if j == i:
                                cum_sum += 1
                        elif j > i:
                                continue
                        else:
                                cum_sum += dp[i - j]
                
                dp[i] = cum_sum
        
        return dp[-1] 
        
print(better_climb_steps(5, {1,2}))
print(climb_steps(5))