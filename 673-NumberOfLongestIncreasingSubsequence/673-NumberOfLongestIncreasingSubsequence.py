# Last updated: 5/6/2025, 11:07:10 pm
class Solution:
    def findNumberOfLIS(self, arr: List[int]) -> int:
        
        n=len(arr)
        lis=[1]*(n)
        count=[1]*n
        ans=1
        for i in range(n-1,-1,-1):
            
            for j in range(n-1,i,-1):
                if arr[j] > arr[i]:
                    if lis[j] + 1 > lis[i]:
                        lis[i] = lis[j] + 1
                        count[i] = 0
                    if lis[j] + 1 == lis[i]:
                        count[i] += count[j]
        ways=0
        target=max(lis)
        for i in range(n):
            if lis[i]==target:
                ways+=count[i]
        return ways
       
        
        
        