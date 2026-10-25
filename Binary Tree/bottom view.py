'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        # code here
        result = {}
        queue = deque()
        queue.append((root, 0))
        while queue:
            e, line = queue.popleft()
            result[line] = e.data
            if e.left:
                queue.append((e.left, line-1))
            if e.right:
                queue.append((e.right, line+1))
        return [result[line] for line in sorted(result)]