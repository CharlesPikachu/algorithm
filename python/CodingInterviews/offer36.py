'''
Function:
    二叉搜索树与双向链表
Author:
    Charles
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return
        self.prev, self.head = None, None
        def recur(root):
            if not root: return
            recur(root.left)
            if self.prev:
                self.prev.right, root.left = root, self.prev
            else:
                self.head = root
            self.prev = root
            recur(root.right)
        recur(root)
        self.head.left, self.prev.right = self.prev, self.head
        return self.head