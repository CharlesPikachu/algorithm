'''
Function:
    斐波那契数列
Author:
    Charles
'''
class Solution:
    memory = {}
    def fib(self, n: int) -> int:
        if n <= 1: return n
        if n not in self.memory:
            self.memory[n] = (self.fib(n-1) + self.fib(n-2)) % 1000000007
        return self.memory[n]