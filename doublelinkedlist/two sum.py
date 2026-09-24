# brute force 


# Structure of Doubly Linked List Node
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def givenSumPairs(self, head, target):
        # code here
        temp = head
        li = []
        nums = []
        while temp is not None:
            li.append(temp.data)
            temp = temp.next
        n = len(li)
        for i in range(0,n):
            for j in range(i+1,n):
                if li[i]+li[j] == target:
                    nums.append([li[i],li[j]])
        return nums

#     i got tle in this 

# Structure of Doubly Linked List Node
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def givenSumPairs(self, head, target):
        # code here
        temp1 = head
        result = []
        while temp1 is not None:
            temp2 = temp1.next
            while temp2 is not None:
                if temp1.data + temp2.data == target:
                    result.append([temp1.data,temp2.data])
                temp2 = temp2.next
            temp1 = temp1.next
        return result

#     again got tle 


# better solution 


# Structure of Doubly Linked List Node
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def givenSumPairs(self, head, target):
        # code here
        temp = head
        my_set = set()
        result = []
        while temp is not None:
            remain = target - temp.data
            if remain in my_set:
                result.append([remain, temp.data])
            my_set.add(temp.data)
            temp = temp.next
        result.sort()
        return result




# optimal solution 

# Structure of Doubly Linked List Node
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def givenSumPairs(self, head, target):
        # code here
        left = head
        right = head
        result = []
        while right.next is not None:
            right = right.next
        while left is not None and right is not None and left.data < right.data:
            total = left.data + right.data
            if total == target:
                result.append([left.data, right.data])
                right = right.prev
                left = left.next
            elif total > target:
                right = right.prev
            else:
                left = left.next
        return result