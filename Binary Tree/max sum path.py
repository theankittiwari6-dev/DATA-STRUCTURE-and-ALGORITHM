# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        maxi = float(-inf)
        def solve(node):
            nonlocal maxi
            if node is None:
                return 0
            lh = solve(node.left)
            if lh < 0:
                lh = 0
            rh = solve(node.right)
            if rh < 0:
                rh = 0
            maxi = max(maxi, lh + node.val + rh)
            return node.val + max(lh, rh)
        solve(root)
        return maxi