# Good morning! Here's your coding interview problem for today.

# This problem was asked by Microsoft.

# A number is considered perfect if its digits sum up to exactly 10.

# Given a positive integer n, return the n-th perfect number.

# For example, given 1, you should return 19. Given 2, you should return 28.
"""

perfect numbers:
19, 28, 37, 46, 55, 64, 73, 82,91, 109, 118
1	

notice that the last digit is 10 - sum of digits
then just add to the back			
"""

def perfect_num(n):
        digit_sum = 0
        temp = n
        while temp:
                last_digit += temp % 10
                temp = temp // 10
        
        last_digit = 10 - digit_sum
        
        result = last_digit
        count = 1
        temp = n
        while n:
                remainder = temp % 10
                result += remainder * (10 ** count)
                temp = temp // 10
                count += 1
        
        return result
        