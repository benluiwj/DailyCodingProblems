# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# An XOR linked list is a more memory efficient doubly linked list. Instead of
# each node holding next and prev fields, it holds a field named both, which is an
# XOR of the next node and the previous node. Implement an XOR linked list; it has
# an add(element) which adds the element to the end, and a get(index) which
# returns the node at index.

# If using a language that has no pointers (such as Python), you can assume you
# have access to get_pointer and dereference_pointer functions that converts
# between nodes and memory addresses.

class Node:
        def __init__(self, value):
                self.value = value
                self.both = 0
        
        def get_pointer(self):
                # gets address
                pass
        
        def dereference_pointer(self):
                # gets node at address
                pass

class LinkedList:
        def __init__(self):
                self.head = None
                self.tail = None
        
        def add(self, Node):
                node_addr = Node.get_pointer()
                if not self.head:
                        self.head = Node
                        self.tail = Node
                        
                
                else:
                        Node.both = self.tail.get_pointer()
                        self.tail.both = self.tail.get_pointer() ^ node_addr
                        self.tail = Node
        
        def index(self, index):
                if index == 0:
                        return self.head
                
                temp_node = self.head
                prev_addr = 0 
                while index:
                        next_node_addr = temp_node.both ^ prev_addr
                        prev_addr = temp_node.get_pointer()
                        temp_node = next_node_addr.dereference_pointer()
                        index -= 1
                
                return temp_node
                        
                
                
        