# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# On our special chessboard, two bishops attack each other if they share the same
# diagonal. This includes bishops that have another bishop located between them,
# i.e. bishops can attack through pieces.

# You are given N bishops, represented as (row, column) tuples on a M by M
# chessboard. Write a function to count the number of pairs of bishops that attack
# each other. The ordering of the pair doesn't matter: (1, 2) is considered the
# same as (2, 1).

# For example, given M = 5 and the list of bishops:

#  * (0, 0)
#  * (1, 2)
#  * (2, 2)
#  * (4, 0)

# The board would look like this:

# [b 0 0 0 0]
# [0 0 b 0 0]
# [0 0 b 0 0]
# [0 0 0 0 0]
# [b 0 0 0 0]


# You should return 2, since bishops 1 and 3 attack each other, as well as bishops
# 3 and 4.

"""

for every bishop count the number of other bishops that fall in line, excluding repeats.

count number of bishops along every diagonal. and for each diagonal, subtract one on the result

the number of attacking pairs of bishops is actuall nC2, where n is the number of bishops along that diagonal.

then for every bishop, take the 2 furthest top corners it can reach and increase the count.

then for each corner, perform nC2
"""

TOP_LEFT_TO_BOTTOM_RIGHT = 0
TOP_RIGHT_TO_BOTTOM_LEFT = 1

def count_bishop_attack(m, bishops):
        counts = dict()
        for r, c in bishops:
                top_lr, top_lc = (r - min(r, c), c - min(r, c))
                top_rr, top_rc = (r - min(r, m - c), c + min(r, m - c))
                
                counts[top_lr, top_lc, TOP_LEFT_TO_BOTTOM_RIGHT] += 1
                counts[top_rr, top_rc, TOP_RIGHT_TO_BOTTOM_LEFT] += 1
        
        result = 0
        for val in counts.values():
                result += (val * (val-1))//2
        
        return result
