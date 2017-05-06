"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    node = head
    visited = [node]

    while True:
        if node.next:
            node = node.next
            if node in visited:
                return True
            else:
                visited.append(node)
        else:
            return False
