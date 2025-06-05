# Last updated: 5/6/2025, 11:08:43 pm
class Solution:
    def minSubArrayLen(self, target: int, arr: List[int]) -> int:
        
        def get_max_sum(k):
            cursum=0
            
            for i in range(k):
                cursum+=arr[i]
            maxx=cursum

            for i in range(len(arr)-k):
                cursum-=arr[i]
                cursum+=arr[i+k]
                maxx=max(cursum,maxx)
            return maxx

        hi=len(arr)
        lo=0
        while(hi>=lo):
            mid=(hi+lo)//2
            sub_sum=get_max_sum(mid)
            if sub_sum<target:
                lo=mid+1
            else:
                hi=mid-1
        if lo<=len(arr):
            return lo 
        else:
            return 0
        
        
        
        
        '''
        i=0
        j=len(nums)-1

        cursum=sum(nums)
        if cursum<target:
            return 0
        while(cursum>target):
            if nums[i]<nums[j]:
                i+=1
                cursum-=nums[i]
            else:
                j-=1
                cursum-=nums[j]
        
        return (j-i+1)

        '''