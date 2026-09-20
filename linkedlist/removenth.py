# brute force 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        temp = head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        if n == count:
            new_head = head.next
            del head
            return new_head
        
        ps = count - n
        target = 0
        temp = head
        while target < ps-1:
            temp = temp.next
            target +=1
        temp.next = temp.next.next
        return head
            

        
# optimal solution 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next
        if fast == None:
            head = head.next
            return head
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head 

        
            
        