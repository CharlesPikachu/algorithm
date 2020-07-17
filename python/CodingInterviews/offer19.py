'''
Function:
    正则表达式匹配
Author:
    Charles
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        first_match = bool(s and p[0] in (s[0], '.'))
        if len(p) > 1 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])