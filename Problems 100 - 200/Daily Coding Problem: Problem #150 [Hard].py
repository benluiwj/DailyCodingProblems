# Good morning! Here's your coding interview problem for today.

# This problem was asked by LinkedIn.

# Given a list of points, a central point, and an integer k, find the nearest k 
# points from the central point.

# For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central
# point (1, 2), and k = 2, return[(0, 0), (3, 1)].

from heapq import *
import math

def k_nearest_from_central(points, central, k):
        central_x, central_y = central
        
        heap = []
        
        for x , y in points:
                dist = math.sqrt(abs(central_x - x) ** 2 + abs(central_y - y) ** 2)
                heappush(heap, (dist, (x,y)))
        
        result = []
        
        for i in range(k):
                _, pt = heappop(heap)
                result.append(pt)
        
        return result

k_nearest_from_central([(0, 0), (5, 4), (3, 1)], (1, 2), 2)