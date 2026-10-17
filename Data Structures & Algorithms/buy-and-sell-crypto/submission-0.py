class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2: return 0
        profit = [0]*n

        for i in range(1,n):
            profit[i] = prices[i] - min(prices[:i])
        return max(profit)