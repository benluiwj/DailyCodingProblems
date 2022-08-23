# Good morning! Here's your coding interview problem for today.

# This problem was asked by Square.

# Assume you have access to a function toss_biased() which returns 0 or 1 with a
# probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the
# bias of the coin.

# Write a function to simulate an unbiased coin toss.


"""

Let's draw out the probability chart for tossing our coin twice. Let's say the probability of getting heads is p, so tails is 1 - p:

HH: p * p
HT: p * (1 - p)
TH: (1 - p) * p
TT: (1 - p) * (1 - p)
Since multiplication is commutative, we find that flipping heads and then tails has the same probability of flipping tails, then heads!


toss coin twice

if heads,tails -> return heads
if tails, heads -> return tails

"""

def toss_bias():
        pass

def unbiased_toss():
        pass