class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        count = {}
        for c in nums:
            count[c] = count.get(c,0) + 1
        
        heap = []
        for n,v in count.items():
            heapq.heappush(heap,(v,n))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for _,num in heap]