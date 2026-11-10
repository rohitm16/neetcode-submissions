class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = {}
        def dp(i):
            if i<0:
                return 0
            if i in mem:
                return mem[i]
            rob = nums[i] + dp(i-2)
            skip = dp(i-1)

            mem[i] = max(rob,skip)
            return mem[i]
        return dp(len(nums)-1)