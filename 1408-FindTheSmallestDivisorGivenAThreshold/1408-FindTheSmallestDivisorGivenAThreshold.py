# Last updated: 5/6/2025, 11:06:30 pm
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(mid):
            s=0
            for ele in nums:
                s+=ele//mid+1
                if ele%mid==0:
                    s-=1
            #print(mid,s)
            return s<=threshold
        lo=1
        hi=10**6+1
        while hi>=lo:
            mid=(lo+hi)//2
            if check(mid):
                
                hi=mid-1
            else:
                lo=mid+1
        return hi+1