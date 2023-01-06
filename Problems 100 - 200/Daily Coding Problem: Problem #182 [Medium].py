# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# A graph is minimally-connected if it is connected and there is no edge that can
# be removed while still leaving the graph connected. For example, any binary tree
# is minimally-connected.

# Given an undirected graph, check if the graph is minimally-connected. You can
# choose to represent the graph as either an adjacency matrix or adjacency list.
from typing import * 

"""
minimal connected - remove any edge disconnects the graph

remove an edge from the graph then perform bfs to see if the graph is still connected. 

assume that graph is a list here, ie dictionary
"""

def minimalConnected(graph):
        start = None
        for key, val in graph:
                if val:
                        graph[key].pop()
                        break
        
        for key, val in graph:
                if val:
                        start = key
                        break
        
        visited = set(start)
        frontier = set(start)
        while frontier:
                new_frontier = set()
                for node in frontier:
                        for neighbor in graph[node]:
                                if neighbor not in visited:
                                        new_frontier.add(neighbor)
                                        visited.add(neighbor)
                
                frontier = new_frontier
        
        return len(visited) == len(graph.keys())
        