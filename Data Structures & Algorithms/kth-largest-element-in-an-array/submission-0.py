class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for _ in nums:
            heapq.heappush(heap, _)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]