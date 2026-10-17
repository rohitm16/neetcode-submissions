class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2: return 0
        profit = [0]*n
        pref = [float("inf")]*n
        pref[0] = prices[0]
        for i in range(1,n):
            pref[i] = min(pref[i-1],prices[i])

        for i in range(1,n):
            profit[i] = prices[i] - pref[i]
        return max(profit)