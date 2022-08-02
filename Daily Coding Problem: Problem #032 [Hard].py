# Good morning! Here's your coding interview problem for today.

# This problem was asked by Jane Street.

# Suppose you are given a table of currency exchange rates, represented as a 2D
# array. Determine whether there is a possible arbitrage: that is, whether there
# is some sequence of trades you can make, starting with some amount A of any
# currency, so that you can end up with some amount greater than A of that
# currency.

# There are no transaction costs and you can trade fractional quantities.

"""

Perform bellman-ford, if weights still change => negative weight cycle
values are all positive -> negate them to use bellman ford

edge as the exchange rate and nodes as currencies. weight is current_currency * exchange rate.

https://anilpai.medium.com/currency-arbitrage-using-bellman-ford-algorithm-8938dcea56ea

"""

from math import log

def arbitrage(graph):
    transformed_graph = [[-log(edge) for edge in row] for row in graph]

    # Pick any source vertex -- we can run Bellman-Ford from any vertex and
    # get the right result
    source = 0
    n = len(transformed_graph)
    min_dist = [float('inf')] * n

    min_dist[source] = 0

    # Relax edges |V - 1| times
    for i in range(n - 1):
        for v in range(n):
            for w in range(n):
                if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
                    min_dist[w] = min_dist[v] + transformed_graph[v][w]

    # If we can still relax edges, then we have a negative cycle
    for v in range(n):
        for w in range(n):
            if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
                return True

    return False