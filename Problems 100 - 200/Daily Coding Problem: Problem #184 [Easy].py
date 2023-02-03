# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Given n numbers, find the greatest common denominator between them.

# For example, given the numbers [42, 56, 14], return 14.
from typing import * 

def gcd(a , b):
    while b:
        t = b
        b = a % b
        a = t
    
    return a


def find_gcd(n):
    if len(n) == 1:
        return n[0]
    return gcd(n[0], find_gcd(n[1:]))

print(find_gcd([42,56,14]))