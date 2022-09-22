# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given a stream of elements too large to store in memory, pick a random element
# from the stream with uniform probability.
import random


def random_element(big_stream):
        for i, val in enumerate(big_stream):
                result = None
                if i == 0:
                        result = val
                
                if random.randint(1, i+1) == i:
                        result = val 
        
        return result