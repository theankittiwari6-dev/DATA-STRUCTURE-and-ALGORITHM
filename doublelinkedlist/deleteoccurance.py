# Structure of the doubly linked list Node 
# class Node:
#     def __init__(self, x):
#         self.data = x
#         self.next = None
#         self.prev = None

class Solution:
    def deleteAllOccurOfX(self, head, x):
        # code her
        temp = head
        while temp is not None:
            if temp.data==x:
                if temp == head:
                    head = head.next
                if temp.prev is not None:
                    temp.prev.next = temp.next
                if temp.next is not None:
                    temp.next.prev = temp.prev
            temp = temp.next
        return head