'''
Function:
    顺时针打印矩阵
Author:
    Charles
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        out = []
        while True:
            # left -> right
            for i in range(left, right+1):
                out.append(matrix[top][i])
            top += 1
            if top > bottom: break
            # top -> bottom
            for i in range(top, bottom+1):
                out.append(matrix[i][right])
            right -= 1
            if left > right: break
            # right -> left
            for i in range(right, left-1, -1):
                out.append(matrix[bottom][i])
            bottom -= 1
            if top > bottom: break
            # bottom -> top
            for i in range(bottom, top-1, -1):
                out.append(matrix[i][left])
            left += 1
            if left > right: break
        return out