'''
Function:
    最长不含重复字符的子字符串
Author:
    Charles
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        dp = [1,] * len(s)
        for i in range(1, len(s)):
            if s[i] not in s[i-dp[i-1]: i]:
                dp[i] = dp[i] + dp[i-1]
            else:
                idx = s[i-dp[i-1]: i].index(s[i])
                dp[i] = dp[i-1] - idx
        return max(dp)