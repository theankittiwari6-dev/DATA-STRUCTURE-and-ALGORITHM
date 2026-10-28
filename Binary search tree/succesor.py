# brute force

'''
Structure of a Binary Search Tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def findPreSuc(self, root, key):
        result = []
        
        def solve(node):
            if node is None:
                return None
            left = solve(node.left)
            result.append(node)
            right = solve(node.right)
        solve(root)
        pre = None
        suc = None
        for node in result:
            if node.data < key:
                pre = node
            if node.data > key and suc is None:
                suc = node
                break
        return [pre, suc]


# optimal 

class Solution:
    def findPreSuc(self, root, key):
        pre = suc = None
        curr = root

        while curr:
            if curr.data < key:
                pre = curr         # candidate predecessor
                curr = curr.right
            elif curr.data > key:
                suc = curr         # candidate successor
                curr = curr.left
            else:
                # key found: use its subtrees if they exist
                if curr.left:
                    t = curr.left
                    while t.right:
                        t = t.right
                    pre = t        # rightmost of left subtree
                if curr.right:
                    t = curr.right
                    while t.left:
                        t = t.left
                    suc = t        # leftmost of right subtree
                break

        return [pre, suc]