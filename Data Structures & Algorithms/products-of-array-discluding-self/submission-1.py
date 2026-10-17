class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zeros = nums.count(0)
        prod = 1
        res = []

        if zeros == 0:
            for i in range(n):
                prod *= nums[i]
            for j in range(n):
                res.append(prod//nums[j])
            return res
        if zeros == 1:
            for i in range(n):
                if nums[i] != 0:
                    prod *= nums[i]
            for j in range(n):
                if nums[j] == 0:
                    res.append(prod)
                else:
                    res.append(0)
            return res
        if zeros > 1:
            res = [0] *n
            return res