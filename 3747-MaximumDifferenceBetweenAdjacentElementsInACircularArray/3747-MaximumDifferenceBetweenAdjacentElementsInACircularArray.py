# Last updated: 12/6/2025, 11:48:06 am
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff=abs(nums[0]-nums[-1])
        n=len(nums)
        for i in range(1,n):
            if abs(nums[i]-nums[i-1])>max_diff:
                max_diff=abs(nums[i]-nums[i-1])
        return max_diff
        