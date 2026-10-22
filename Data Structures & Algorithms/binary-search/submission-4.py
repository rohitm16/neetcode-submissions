class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        h = n-1

        while l<=h:
            i = (l + h)//2
            if target < nums[i]:
                h = i-1
            elif target > nums[i]:
                l = i+1
            elif target == nums[i]:
                return i
        return -1
