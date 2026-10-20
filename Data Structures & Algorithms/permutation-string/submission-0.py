class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        l=0
        r = n-1
        while r <len(s2):
            if sorted(s2[l:r+1]) == sorted(s1):
                return True
            l += 1
            r += 1
        return False
        