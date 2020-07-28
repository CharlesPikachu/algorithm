'''
Function:
    二叉树中和为某一值的路径
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
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        paths = []
        def dfs(root, sum, path):
            if not root: return
            if (sum - root.val == 0) and not (root.left or root.right):
                path.append(root.val)
                paths.append(path.copy())
            path.append(root.val)
            dfs(root.left, sum-root.val, path.copy())
            dfs(root.right, sum-root.val, path.copy())
            path.pop(-1)
        dfs(root, sum, [])
        return paths