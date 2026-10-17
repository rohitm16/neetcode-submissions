class Solution:
    def maxArea(self, nums: List[int]) -> int:
        gmax = 0
        n = len(nums)
        i = 0
        j = n-1
        while i < j:
            w = min(nums[i],nums[j])*(j-i)
            gmax = max(gmax,w)
            if nums[i] < nums[j]:
                i += 1
            else:
                j -= 1
        return gmax