# Last updated: 5/6/2025, 11:06:03 pm
class Solution:
    def isZeroArray(self, arr: List[int], queries: List[List[int]]) -> bool:
        n=len(arr)
        pref=[0]*(n+1)
        #pref[i] is sum from 0...i 
        #pref[0] is always 0 
        #for i in range(n):
        #    pref[i+1]=pref[i]+arr[i]
        for l,r in queries: 
            pref[l+1]-=1
            if r+2<=n:
                pref[r+2]+=1
        #deltas=[0]*n
        for i in range(1,n+1):
            pref[i]+=pref[i-1]
        #print(pref)
        count=0
        #print(pref)
        for i in range(1,n+1):
            if arr[i-1]+pref[i]<=0:
                count+=1
        #print(count)
        return count==n