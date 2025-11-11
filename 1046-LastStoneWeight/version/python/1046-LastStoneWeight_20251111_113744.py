# Last updated: 11/11/2025, 11:37:44
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[-x for x in stones]
        heapify(heap)
        while len(heap)>1:
            x=-heappop(heap)
            y=-heappop(heap)
            new_wt=abs(x-y)
            if new_wt!=0:
                heappush(heap,-new_wt)
        if len(heap)==0:
            return 0 
        return -heappop(heap)
        