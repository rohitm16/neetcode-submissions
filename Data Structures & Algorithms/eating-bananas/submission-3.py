class Solution:
    def minEatingSpeed(self, piles: List[int], p: int) -> int:
        l = 0
        h = max(piles)
        m = (l+h+1)//2

        while l<h-1:
            k = 0
            for i in piles:
                k += (i+m-1)//m
            
            if k>p:
                l = m
            else:
                h = m

            m = (l+h+1)//2

        
        return h


            