# Last updated: 11/11/2025, 11:55:15
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=nums[:]
        heapify(heap)
        while len(heap)>k:
            heappop(heap)
        return heap[0]