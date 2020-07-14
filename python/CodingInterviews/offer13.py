'''
Function:
    机器人的运动范围
Author:
    Charles
'''
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def isvalid(x, y):
            s = 0
            for i in str(x)+str(y): s += int(i)
            return s <= k
        flags = [[0,] * n for _ in range(m)]
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n: return
            if (not isvalid(x, y)) or flags[x][y]: return
            flags[x][y] = 1
            dfs(x+1, y)
            dfs(x, y+1)
            dfs(x-1, y)
            dfs(x, y-1)
        dfs(0, 0)
        count = sum([sum(each) for each in flags])
        return count