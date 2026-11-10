class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        def dp(i):
            if i == 0:
                return cost[0]
            if i == 1:
                return cost[1]
            if i in memo:
                return memo[i]
            memo[i] = cost[i] + min(dp(i-1),dp(i-2))

            return memo[i]
        return min(dp(n-2), dp(n-1))

