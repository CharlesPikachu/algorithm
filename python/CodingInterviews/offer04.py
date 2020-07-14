'''
Function:
    二维数组中的查找
Author:
    Charles
'''
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        num_rows, num_cols = len(matrix), len(matrix[0])
        row, col = num_rows - 1, 0
        while row >= 0 and col < num_cols:
            num = matrix[row][col]
            if num == target: return True
            elif num > target: row -= 1
            else: col += 1
        return False