class Solution:
    def minEatingSpeed(self, piles: List[int], p: int) -> int:
        l = 1
        import math
        h = max(piles)
        m = (l+h)//2

        while l<h:
            k = 0
            m = (l+h)//2        
            for v in piles:
                k += math.ceil(v/m)           
            if k>p:
                l = m+1
            else:
                h = m
        return h



            