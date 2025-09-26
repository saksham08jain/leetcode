# Last updated: 26/09/2025, 09:42:32
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        lo=0 
        hi=n-1 
        while hi>=lo:
            mid=(hi+lo)//2
            if nums[mid]>target:
                hi=mid-1 
            elif nums[mid]<target:
                lo=mid+1
            else:
                return mid 
        return -1
        