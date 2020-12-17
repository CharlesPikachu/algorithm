'''
Function:
    数组中的逆序对
Author:
    Charles
'''
class Solution:
    def firstUniqChar(self, s: str) -> str:
        count = {}
        for c in s:
            count[c] = c not in count
        for key, value in count.items():
            if value: return key
        return ' '