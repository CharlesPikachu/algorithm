'''
Function:
    从上到下打印二叉树 III
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
        res, queue, flag = [], [[root]], True
        while queue:
            res_lvl, next_lvl, nodes = [], [], queue.pop(0)
            for node in nodes:
                res_lvl.append(node.val)
                if node.left: next_lvl.append(node.left)
                if node.right: next_lvl.append(node.right)
            if not flag: res_lvl = res_lvl[::-1]
            if next_lvl: queue.append(next_lvl)
            if res_lvl: res.append(res_lvl)
            flag = not flag
        return res