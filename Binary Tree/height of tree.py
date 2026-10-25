# recursive approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        def solve(node):
            if node == None:
                return 0
            lh = solve(node.left)
            rh = solve(node.right)
            return 1 + max(lh, rh)
        return solve(root)



# iterative approach 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        queue = deque([])
        height = 0
        queue.append(root)
        while len(queue) != 0:
            height+=1
            for _ in range(len(queue)):
                e = queue.popleft()
                if e.left is not None:
                    queue.append(e.left)
                if e.right is not None:
                    queue.append(e.right)
        return height

        