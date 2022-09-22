# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Implement an LRU (Least Recently Used) cache. It should be able to be
# initialized with a cache size n, and contain the following methods:

#  * set(key, value): sets key to value. If there are already n items in the cache
#    and we are adding a new item, then it should also remove the least recently
#    used item.
#  * get(key): gets the value at key. If no such key exists, return null.

# Each operation should run in O(1) time.

from typing import *

"""

when there are n items, pop operation is O(1). deletion is O(n) since shift everything forward. append to back is O(1)

use a doubly-linked list. create a dictionary that maps the value to the node itself, then deletion would be O(1).


"""
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        # dummy nodes
        self.head = Node(None, 'head')
        self.tail = Node(None, 'tail')
        # set up head <-> tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def get_head(self):
        return self.head.next

    def get_tail(self):
        return self.tail.prev

    def add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

class LRUCache:
    def __init__(self, n):
        self.n = n
        self.dict = {}
        self.list = LinkedList()

    def put(self, key, val):
        if key in self.dict:
            self.dict[key].delete()
        n = Node(key, val)
        self.list.add(n)
        self.dict[key] = n
        if len(self.dict) > self.n:
            head = self.list.get_head()
            self.list.remove(head)
            del self.dict[head.key]

    def get(self, key):
        if key in self.dict:
            n = self.dict[key]
            # bump to the back of the list by removing and adding the node
            self.list.remove(n)
            self.list.add(n)
            return n.val
            
            
            
                


cache1 = LRUCache(1)
cache1.put(2,1)
cache1.get(2)


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1
cache.put(3,3)
assert cache.get(2) == None
cache.put(4, 4);

assert cache.get(1) == None;    
assert cache.get(3) == 3;    
assert cache.get(4) == 4 ;
        
        
        
        