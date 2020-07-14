'''
Function:
    青蛙跳台阶问题
Author:
    Charles
'''
class Solution:
    memory = {}
    def numWays(self, n: int) -> int:
        if n <= 1: return 1
        if n not in self.memory:
            self.memory[n] = (self.numWays(n-1) + self.numWays(n-2)) % 1000000007
        return self.memory[n]