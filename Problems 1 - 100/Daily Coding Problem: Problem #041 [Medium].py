# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given an unordered list of flights taken by someone, each represented as
# (origin, destination) pairs, and a starting airport, compute the person's
# itinerary. If no such itinerary exists, return null. If there are multiple
# possible itineraries, return the lexicographically smallest one. All flights
# must be used in the itinerary.

# For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL',
# 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list
# ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

# Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport
# 'COM', you should return null.

# Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and
# starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even
# though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first
# one is lexicographically smaller.

from typing import *

"""

creating a mapping of airports origin to destination
create a visited table -> cannot go if already visited
concatenate strings then compare to get lexi smallest using min
split it up after

"""


class Solution(object):
        def findItinerary(self, tickets, start):

                
                # create origin to dest mappings
                airport_mapppings = dict()
                
                visited = set()
                
                for origin, dest in tickets:
                        if origin in airport_mapppings:
                                airport_mapppings[origin].append(dest)
                        
                        else:
                                airport_mapppings[origin] = [dest]
                        
                        visited.add((origin, dest))
                                
                                             
                
                result = []
                
                def helper(start, current):
                        if not visited:
                                result.append(current[::])
                                return
                        
                        collected_paths = []
                        
                        for i, destination in enumerate(airport_mapppings[start]):
                                tix_tuple = (start, destination)
                                if tix_tuple in visited:
                                        visited.remove(tix_tuple)
                                        airport_mapppings[start].pop(i)
                                        current.append(destination)
                                        helper(destination, current)
                                        current.pop()
                                        airport_mapppings[start].insert(i, destination)
                                        visited.add(tix_tuple)
                        
                        return collected_paths
                
                if start not in airport_mapppings:
                        return
                
                helper(start, [start])
                
                string_res = []
                for itinery in result:
                        string_res.append(' '.join(itinery))
                
                lexi_lowest = min(string_res)
                
                return lexi_lowest.split()

sol = Solution()

sol.findItinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A')