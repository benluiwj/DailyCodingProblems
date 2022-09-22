# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a
# Monte Carlo method.

# Hint: The basic equation of a circle is x2 + y2 = r2.
import random

def estimate_pi() :
        count = 0
        in_quadrant = 0
        
        for _ in range(1000000):
                x = random.random()
                y = random.random()
                if x ** 2 + y ** 2 < 1:
                        in_quadrant += 1
                count += 1
        
        return round(in_quadrant * 4/count, 3)

print(estimate_pi())