class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        si = [ord(x) for x in s]
        si.sort()
        ti = [ord(y) for y in t]
        ti.sort()

        if si == ti:
            return True
        return False