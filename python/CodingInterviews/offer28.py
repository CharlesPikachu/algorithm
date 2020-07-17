'''
Function:
    对称的二叉树
Author:
    Charles
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        def recur(left, right):
            if not left: return not right
            if not right: return not left
            if left.val != right.val: return False
            return recur(left.left, right.right) and recur(left.right, right.left)
        return recur(root.left, root.right)