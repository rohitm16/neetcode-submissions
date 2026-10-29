class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = []
        res = []
        n = len(nums)

        def back(i):
            if i == n:
                res.append(arr.copy())
                return

            back(i+1)
            
            arr.append(nums[i])
            back(i+1)
            arr.pop()

        back(0)
        return res