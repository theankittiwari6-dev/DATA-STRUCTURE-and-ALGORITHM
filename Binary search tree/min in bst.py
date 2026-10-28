"""
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def minValue(self, root):
        # code here
        mini = root
        while mini is not None and mini.left is not None:
            mini = mini.left
        return mini.data