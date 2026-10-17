class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # n = len(numbers)
        # dp = []
        # for i in range(n):
        #     dp.setdefault(numbers[i],[])append(i)
        seen = {}

        for i,x in enumerate(numbers):
            req = target -x
            if req in seen:
                return ([seen[req]+1,i+1])
            seen[x] = i
        