'''
Function:
    剪绳子
Author:
    Charles
'''
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3: return n - 1
        nums = []
        while n >= 3:
            n -= 3
            nums.append(3)
        if n == 2: nums.append(2)
        else: nums.append(n+nums.pop())
        res = 1
        for n in nums: res *= n
        return res


class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [1,] * (n + 1)
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(j, dp[j]) * max(i-j, dp[i-j]))
        return dp[-1]