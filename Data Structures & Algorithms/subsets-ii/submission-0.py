class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = []
        res = []
        n = len(nums)

        def back(i):
            res.append(arr.copy())

            for k in range(i, n):

                if k > i and nums[k] == nums[k-1]:
                    continue

                arr.append(nums[k])
                back(k+1)
                arr.pop()

        back(0)
        return res