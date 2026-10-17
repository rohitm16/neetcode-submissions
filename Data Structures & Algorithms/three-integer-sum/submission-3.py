class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()

        for i in range(n):
            seen = set()
            for j in range(i+1,n):
                req = - nums[i] - nums[j]
                if req in seen:
                    t = tuple(sorted((nums[i],nums[j],req)))
                    res.add(t)
                seen.add(nums[j])
        return [list(r) for r in res]
