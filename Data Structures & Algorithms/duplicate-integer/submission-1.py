class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = {}
        for n in nums:
            l[n] = l.get(n,0)+1
        for v in l.values():
            if v>1:
                return True
        return False