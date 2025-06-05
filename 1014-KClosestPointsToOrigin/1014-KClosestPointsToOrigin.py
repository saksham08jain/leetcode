# Last updated: 5/6/2025, 11:06:41 pm
from heapq import * 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap=[]
        for point in points:
            distance=point[0]**2+point[1]**2
            
            if len(maxheap)==k:
                dist=-1*maxheap[0][0]
                if(distance<dist):
                    heappop(maxheap)
                    heappush(maxheap,(-distance,point))
            else:
                heappush(maxheap,(-distance,point))

        print(maxheap)
        li=[]
        for i in range(k):
            
            li.append(heappop(maxheap)[1])
        return li