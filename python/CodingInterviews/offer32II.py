'''
Function:
    从上到下打印二叉树 II
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, queue = [], [[root]]
        while queue:
            nodes, res_lvl, next_lvl = queue.pop(0), [], []
            for node in nodes:
                res_lvl.append(node.val)
                if node.left: next_lvl.append(node.left)
                if node.right: next_lvl.append(node.right)
            if next_lvl: queue.append(next_lvl)
            if res_lvl: res.append(res_lvl)
        return res