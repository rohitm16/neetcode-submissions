class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        dp_l = [0]*n
        dp_l[0] = height[0]
        dp_r = [0]*n
        dp_r[-1] = height[-1]
        dp_m = []

        for i in range(1,n):
            dp_l[i] = max(dp_l[i-1],height[i])
        
        for j in range(n-2,-1,-1):
            dp_r[j] = max(dp_r[j+1],height[j])
        w = 0
        for k in range(n):
            w += max(0, min(dp_r[k],dp_l[k])-height[k])

        return w