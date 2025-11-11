# Last updated: 11/11/2025, 11:46:42
class Solution:
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def p2key(point):
            return (point[0]**2+point[1]**2)
        heap=[(p2key(x),x) for x in points]
        heapify(heap)
        ans=[]
        while k:
            k-=1
            ans.append(heappop(heap)[1])
        return ans

