# Last updated: 5/6/2025, 11:07:01 pm
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo=-1
        hi=len(nums)
        mid=(lo+hi)//2

        while(mid>lo and mid<hi):

            if nums[mid]<target:
                lo=mid 
            elif nums[mid]==target:
                return mid
            else:
                hi=mid
            mid=(lo+hi)//2
        return -1