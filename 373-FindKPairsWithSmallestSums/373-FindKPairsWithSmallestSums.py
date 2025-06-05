# Last updated: 5/6/2025, 11:07:48 pm
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Initialize the min-heap
        min_heap = []
        result = []
        
        # Push the first k pairs of (nums1[i], nums2[0]) onto the heap
        # We push the sum, and the indices i and 0
        for i in range(min(k, len(nums1))):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
        
        # Extract the smallest pairs from the heap k times
        while k > 0 and min_heap:
            # Pop the smallest element from the heap
            current_sum, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            
            # If there are more elements in nums2 to pair with nums1[i], push them onto the heap
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
            
            k -= 1
        
        return result
