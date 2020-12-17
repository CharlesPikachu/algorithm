'''
Function:
    股票的最大利润
Author:
    Charles
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        dp = [0,] * len(prices)
        min_ = prices[0]
        for i in range(1, len(prices)):
            dp[i] = max(dp[i-1], prices[i] - min_)
            if min_ > prices[i]: min_ = prices[i]
        return dp[-1]