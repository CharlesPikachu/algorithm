'''
Function:
    数据流中的中位数
Author:
    Charles
'''
from heapq import *

class MedianFinder:
    def __init__(self):
        self.A, self.B = [], []
    def addNum(self, num: int) -> None:
        if len(self.A) != len(self.B):
            heappush(self.A, num)
            heappush(self.B, -heappop(self.A))
        else:
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))
    def findMedian(self) -> float:
        if not self.A: return []
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0