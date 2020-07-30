'''
Function:
    字符串的排列
Author:
    Charles
'''
class Solution:
    def permutation(self, s: str) -> List[str]:
        res, s = [], list(s)
        def dfs(boundary):
            if boundary == len(s) - 1: return res.append(''.join(s))
            dic = set()
            for i in range(boundary, len(s)):
                if s[i] in dic: continue
                dic.add(s[i])
                s[i], s[boundary] = s[boundary], s[i]
                dfs(boundary+1)
                s[i], s[boundary] = s[boundary], s[i]
        dfs(0)
        return list(res)