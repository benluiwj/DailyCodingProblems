# Good morning! Here's your coding interview problem for today.

# This question was asked by Google.

# Given an integer n and a list of integers l, write a function that randomly
# generates a number from 0 to n-1 that isn't in l (uniform).

import random

"""
generate numbers till we find one that isnt in l. Possible infinite worsetime

just do it naively; create a list from 0 to n-1 that subtract elements that are in l...

"""

def uniform_generator(n, l):
        while True:
                generated_num = random.randint(0, n-1)
                if generated_num not in l:
                        return generated_num