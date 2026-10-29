class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        res = [0] * n
        st = []

        for i in range(n):
            while st and temp[i] > temp[st[-1]]:
                prev = st.pop()
                res[prev] = i - prev

            st.append(i)
        return res
