# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given a function that generates perfectly random numbers between 1 and k
# (inclusive), where k is an input, write a function that shuffles a deck of cards
# represented as an array using only swaps.

# It should run in O(N) time.

# Hint: Make sure each one of the 52! permutations of the deck is equally likely.

import random

"""

Fisher-Yates shuffle

Our loop invariant will be the following: at each index i of our loop, all indices before i have an equally random probability of being any element from our array.

"""

def shuffle_deck(cards):
        n = len(cards)
        for i in range(n-1):
                j = random.randint(i, n-1)
                cards[i], cards[j] = cards[j], cards[i]