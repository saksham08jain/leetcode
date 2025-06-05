# Last updated: 5/6/2025, 11:08:36 pm
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        count=[0]*(10**5+1)
        n=len(nums)
        k=n-k+1
        for i in range(n):
            nums[i]+=10**4
        for i in range(n):
            count[nums[i]]+=1
        for i in range(1,10**5):
            count[i]+=count[i-1]
        lo=0 
        hi=10**5
        while hi>=lo:
            mid=(hi+lo)//2
            
            if count[mid]>=k:
                hi=mid-1

            else:
                lo=mid+1
        return(hi+1-10**4)