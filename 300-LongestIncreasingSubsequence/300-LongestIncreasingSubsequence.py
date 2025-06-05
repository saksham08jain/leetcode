# Last updated: 5/6/2025, 11:08:08 pm
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        sub=[]
        sub.append(arr[0])
        n=len(arr)
        for i in range(len(arr)):
            #print(sub,arr[i])
            if arr[i]>sub[-1]:
                sub.append(arr[i])
            elif arr[i]<sub[-1]:
                idx=bisect_left(sub,arr[i])
                sub[idx]=arr[i]
        return len(sub)
            


        
        
        