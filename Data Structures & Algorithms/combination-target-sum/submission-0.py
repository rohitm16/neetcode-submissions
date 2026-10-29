class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        arr = []
        n = len(nums)
        def back(start,rem):
            if rem == 0:
                res.append(arr.copy())
                return

            for i in range(start,len(nums)):
                if nums[i] > rem:
                    continue
                arr.append(nums[i])
                back(i,rem - nums[i])
                arr.pop()

        back(0,target)
        return res
            