# brute force 



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            n = len(queue)
            for i in range(n):
                e = queue.popleft()
                if i == n-1:
                    ans.append(e.val)
                if e.left:
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)
        return ans



# optimal solution 



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
       
        result = []
        def solve(node, level):
            if node is None:
                return 
            if len(result) == level:
                result.append(node.val)
            if node.right:
                solve(node.right, level+1)
            if node.left:
                solve(node.left, level+1)
        solve(root, 0)
        return result