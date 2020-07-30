'''
Function:
    1～n整数中1出现的次数
Author:
    Charles
'''
class Solution:
    def countDigitOne(self, n: int) -> int:
        digital, count = 1, 0
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:
            if cur == 0: count += high * digital
            elif cur == 1: count += high * digital + low + 1
            else: count += (high + 1) * digital
            low, cur, high = cur * digital + low, high % 10, high // 10
            digital *= 10
        return count