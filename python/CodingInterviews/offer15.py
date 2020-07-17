'''
Function:
    二进制中1的个数
Author:
    Charles
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count