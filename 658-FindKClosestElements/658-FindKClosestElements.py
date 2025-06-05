# Last updated: 5/6/2025, 11:07:11 pm
from bisect import bisect_left
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        newarr=[-float('inf')]
        newarr.extend(arr)
        arr=newarr
        gex_idx=bisect_left(arr,x)
        
        '''
        if abs(x-arr[gex_idx-1])<=abs(x-arr[gex_idx]):#gex_idx maybe out of bounds
            closest_idx=gex_idx-1
        else:
            closest_idx=gex_idx
        '''
        i=gex_idx
        j=gex_idx-1
        closest=[]

        while(len(closest)<k):
            if (i<0 or i>len(arr)-1) or x-arr[j]<=arr[i]-x:
                closest.append(arr[j])
                j-=1 
            else:
                closest.append(arr[i])
                i+=1
        return sorted(closest)