'''
Function:
    二叉搜索树的后序遍历序列
Author:
    Charles
'''
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def recur(i, j):
            if i > j: return True
            p = i
            while postorder[p] < postorder[j]: p += 1
            left = p
            while postorder[p] > postorder[j]: p += 1
            return p == j and recur(i, left-1) and recur(left, j-1)
        return recur(0, len(postorder)-1)