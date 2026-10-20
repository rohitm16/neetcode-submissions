class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        maxl = 0
        l = 0
        cnt = {}

        for r in range(n):
            cnt[s[r]] = cnt.get(s[r], 0) + 1

            length = r - l + 1
            maxf = max(cnt.values())

            while length - maxf > k:
                cnt[s[l]] -= 1
                l += 1
                length = r - l + 1
                maxf = max(cnt.values())

            maxl = max(maxl, length)

        return maxl