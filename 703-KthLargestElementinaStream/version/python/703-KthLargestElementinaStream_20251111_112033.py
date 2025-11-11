# Last updated: 11/11/2025, 11:20:33
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #minheap 
        self.heap=nums 
        heapify(self.heap)
        self.size=k 

    def add(self, val: int) -> int:
        heappush(self.heap,val)
        while len(self.heap)>self.size:
            heappop(self.heap)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)