'''
Function:
    栈的压入、弹出序列
Author:
    Charles
'''
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        while True:
            if not pushed:
                break
            stack.append(pushed.pop(0))
            while stack and (popped[0] == stack[-1]):
                popped.pop(0)
                stack.pop()
        return True if not stack else False