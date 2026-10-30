class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        arr = []
        res = []

        def backtracking(rem,i):
            if rem == 0:
                res.append(arr.copy())
                return
            
            for k in range(i,n):
                if candidates[k] > rem:
                    continue
                if k > i and candidates[k] == candidates[k-1]:
                    continue
                arr.append(candidates[k])
                backtracking(rem-candidates[k],k+1)
                arr.pop()
        backtracking(target,0)
        return res
        
        