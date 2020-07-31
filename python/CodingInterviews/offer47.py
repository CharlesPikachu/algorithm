'''
Function:
    礼物的最大价值
Author:
    Charles
'''
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        dp = [[0,] * num_cols for _ in range(num_rows)]
        for i in range(num_rows):
            for j in range(num_cols):
                if i == 0 and j == 0: dp[i][j] = grid[i][j]
                elif i == 0: dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0: dp[i][j] = dp[i-1][j] + grid[i][j]
                else: dp[i][j] = max(dp[i][j-1] + grid[i][j], dp[i-1][j] + grid[i][j])
        return dp[-1][-1]