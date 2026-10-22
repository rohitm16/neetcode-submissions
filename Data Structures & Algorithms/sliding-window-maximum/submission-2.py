class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        maxH = [(-nums[i],i) for i in range(k)]
        heapq.heapify(maxH)
        res = [-maxH[0][0]]

        for i in range(k,len(nums)):
            heapq.heappush(maxH, (-nums[i],i))
            
            while maxH[0][1] <= i-k:
                heapq.heappop(maxH)
            res.append(-maxH[0][0])
        return res