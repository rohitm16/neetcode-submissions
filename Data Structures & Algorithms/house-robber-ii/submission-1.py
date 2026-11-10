class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(arr):
            mem = {}
            def dp(i):
                if i<0:
                    return 0
                if i in mem:
                    return mem[i]
                rob = arr[i] + dp(i-2)
                skip = dp(i-1)

                mem[i] = max(rob,skip)
                return mem[i]
            return dp(len(arr)-1)     
        if len(nums) == 1:
            return nums[0]   
        return max(solve(nums[1:]), solve(nums[:-1]))