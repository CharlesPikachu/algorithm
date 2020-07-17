'''
Function:
    包含min函数的栈
Author:
    Charles
'''
class MinStack:
    def __init__(self):
        self.A = []
        self.B = []
    def push(self, x: int) -> None:
        self.A.append(x)
        if not self.B:
            self.B.append(x)
        else:
            if self.B[-1] >= x: self.B.append(x)
    def pop(self) -> None:
        if self.A: n = self.A.pop()
        if n == self.B[-1]: self.B.pop()
    def top(self) -> int:
        return self.A[-1]
    def min(self) -> int:
        return self.B[-1]