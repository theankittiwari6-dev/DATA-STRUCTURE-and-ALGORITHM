# class Node:
#     def __init__(self, value):
#         self.data = value  # value stored in node
#         self.next = None
#         self.prev = None

class Solution:
    def removeDuplicates(self, headRef):
        if headRef is None:
            return None

        temp = headRef

        while temp.next is not None:
            if temp.data == temp.next.data:
                duplicate = temp.next

                temp.next = duplicate.next

                if duplicate.next is not None:
                    duplicate.next.prev = temp
            else:
                temp = temp.next

        return headRef