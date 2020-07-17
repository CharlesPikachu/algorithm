'''
Function:
    打印从1到最大的n位数
Author:
    Charles
'''
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        start, end = 1, 10 ** n
        return list(range(start, end))