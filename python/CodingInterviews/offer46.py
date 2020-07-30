'''
Function:
    把数字翻译成字符串
Author:
    Charles
'''
class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        a, b = 1, 1
        for i in range(2, len(num)+1):
            a, b = (a + b if '10' <= num[i-2: i] <= '25' else a), a
        return a