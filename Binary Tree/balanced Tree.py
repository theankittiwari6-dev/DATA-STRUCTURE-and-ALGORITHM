# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        balanced = True
        def solve(node):
            nonlocal balanced
            if node == None:
                return 0
            lh = solve(node.left)
            rh = solve(node.right)
            hight_diff = abs(lh-rh)
            if hight_diff > 1:
                balanced = False
            return 1 + max(lh, rh)
        solve(root)
        return balanced
        