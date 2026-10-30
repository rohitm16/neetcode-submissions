class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        arr = []
        res = []
        visited = [False] * n

        def backtracking(k):
            if k == n:
                res.append(arr.copy())
                return

            for i in range(n):
                if visited[i]:
                    continue

                arr.append(nums[i])
                visited[i] = True
                backtracking(k+1)
                arr.pop()
                visited[i] = False

        backtracking(0)
        return res


