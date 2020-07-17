'''
Function:
    数值的整数次方
Author:
    Charles
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x, n = 1./x, -n
        res = 1
        while n:
            if n & 1: res *= x
            x *= x
            n >>= 1
        return res