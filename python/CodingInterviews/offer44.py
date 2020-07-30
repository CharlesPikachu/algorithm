'''
Function:
    数字序列中某一位的数字
Author:
    Charles
'''
class Solution:
    def findNthDigit(self, n: int) -> int:
        num_digitals, start, end = 1, 0, 10
        while True:
            length = (end - start) * num_digitals
            if n - length < 0:
                break
            n = n - length
            start, end, num_digitals = end, end * 10, num_digitals + 1
        digital = start + n // num_digitals
        return int(str(digital)[n % num_digitals])