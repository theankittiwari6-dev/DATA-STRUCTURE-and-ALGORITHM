# brute force 


""" Structure of Doubly Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        # code here
        temp = head
        stack = []
        while temp is not None:
            stack.append(temp.data)
            temp = temp.next
        temp = head
        while temp is not None:
            e = stack.pop()
            temp.data = e
            temp = temp.next
        return head



# optimal solution 


""" Structure of Doubly Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        # code here
        prev = None
        temp = head
        while temp is not None:
            first = temp.next
            temp.next = prev
            temp.prev = first
            prev = temp
            temp = first
        return prev