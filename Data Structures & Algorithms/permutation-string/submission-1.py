class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if len(s2) < n:
            return False
        cnt1 = {}
        cnt2 = {}
        for c in s1:
            cnt1[c] = cnt1.get(c,0) + 1
        for i in range(n):
            cnt2[s2[i]] = cnt2.get(s2[i],0) + 1
        if cnt1 == cnt2:
            return True

        l = 0
        r = n
        while r < len(s2):
            cnt2[s2[r]] = cnt2.get(s2[r],0) + 1
            cnt2[s2[l]] -= 1
            if cnt2[s2[l]] == 0:
                del cnt2[s2[l]]
            l += 1
            r += 1
            if cnt1 == cnt2:
                return True
        return False

