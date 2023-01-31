# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# You are given a starting state start, a list of transition probabilities for a
# Markov chain, and a number of steps num_steps. Run the Markov chain starting
# from start for num_steps and compute the number of times we visited each state.

# For example, given the starting state a, number of steps 5000, and the following
# transition probabilities:

# [
#   ('a', 'a', 0.9),
#   ('a', 'b', 0.075),
#   ('a', 'c', 0.025),
#   ('b', 'a', 0.15),
#   ('b', 'b', 0.8),
#   ('b', 'c', 0.05),
#   ('c', 'a', 0.25),
#   ('c', 'b', 0.25),
#   ('c', 'c', 0.5)
# ]


# One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656,
# 'c': 332 }.
from typing import * 
from random import *

def markov_chain(starting_state, steps, transition_probs):
    # step 1: convert the transition probs to a dictionary
    mappings = dict()
    result = dict()
    for src, dst, prob in transition_probs:
        if src not in mappings:
            mappings[src] = []
        
        mappings[src].append([dst, prob])
        result[src] = 0
    
    current = starting_state
    
    for _ in range(steps):
        # step 2: get a random value
        next_step = random()
        result[current] += 1
        
        # step 3:
        for dst, prob in mappings[current]:
            next_step -= prob
            if next_step <= 0:
                current = dst
    
    return result
        