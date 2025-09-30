# Last updated: 30/09/2025, 17:55:45
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo=0 
        n=len(nums)
        hi=n-1

        while hi>=lo:
            mid=(hi+lo)//2
            # print(mid)
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[lo]:
                # this part of array is sorted ie the part between lo and mid 
                # check if this part contains target 
                if target<=nums[mid] and target>=nums[lo]:
                    # search this part further
                    hi=mid-1 
                else:               
                    lo=mid+1
            else:
                # the other part must be sorted 
                # check if that part contains target 
                # if nums[hi]>nums[mid]:
                if target>=nums[mid] and target<=nums[hi]:
                    # search this part 
                    lo=mid+1 
                else:
                    # saecrth the other part 
                    hi=mid-1
        return -1

