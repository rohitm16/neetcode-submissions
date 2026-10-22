class Solution:
    def searchMatrix(self, nums: List[List[int]], target: int) -> bool:

        if not nums or not nums[0]:
            return False

        n = len(nums)
        m = len(nums[0])
        l, h = 0, n-1

        while l<=h:
            i = (l+h)//2
            if target<nums[i][0]:
                h = i-1
            elif target > nums[i][m-1]:
                l = i+1
            else:
                l1, h1 = 0, m-1
                while l1<= h1:
                    i1 = (l1+h1)//2
                    if target < nums[i][i1]:
                        h1 = i1-1
                    elif target > nums[i][i1]:
                        l1 = i1+1
                    else:
                        return True
                return False
        return False


        