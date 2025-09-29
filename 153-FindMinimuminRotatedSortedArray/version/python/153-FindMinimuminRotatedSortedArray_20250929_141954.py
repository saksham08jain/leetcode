# Last updated: 29/09/2025, 14:19:54
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        lo=0 
        hi=n-1
        a0=nums[0]
        ans=a0
        while hi>=lo:
            mid=(hi+lo)//2
            # print(mid)
            if nums[mid]>=a0:
                # fgo right 
                lo=mid+1 
            else:
                hi=mid-1 
                ans=min(nums[mid],ans)
        return ans

        