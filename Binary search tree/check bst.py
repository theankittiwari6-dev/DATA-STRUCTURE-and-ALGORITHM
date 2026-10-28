# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        result = []
        curr = root
        while curr:
            if curr.left is None:
                result.append(curr.val)
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right is not curr:
                    pred = pred.right
                if pred.right is None:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    result.append(curr.val)
                    curr = curr.right
        return result == sorted(result) and len(result) == len(set(result))




# better solution 



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        result = []
        curr = root
        while curr:
            if curr.left is None:
                result.append(curr.val)
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right is not curr:
                    pred = pred.right
                if pred.right is None:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    result.append(curr.val)
                    curr = curr.right
        for i in range(1, len(result)):
            if result[i] <= result[i-1]:
                return False
        return True





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        prev = None
        valid = True
        curr = root
        while curr:
            if curr.left is None:
                if prev is not None and curr.val <= prev:
                    valid = False
                prev = curr.val 
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right is not curr:
                    pred = pred.right
                if pred.right is None:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    if prev is not None and curr.val <= prev:
                        valid = False
                    prev = curr.val 
                    curr = curr.right
        return valid







# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def solve(node, limit):
            if not node:
                return True
            if not limit[0]<node.val<limit[1]:
                return False
            left = solve(node.left, [limit[0], node.val])
            if left == False:
                return False
            right = solve(node.right, [node.val, limit[1]])
            return left and right
        return solve(root, [float("-inf"), float("inf")])