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