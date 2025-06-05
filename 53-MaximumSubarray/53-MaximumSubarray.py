# Last updated: 5/6/2025, 11:10:11 pm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #if max(nums)<0:
        #    return max(nums)
        prev=float('-inf')
        maxx=float('-inf')
        for i in range(1,len(nums)+1):
            prev=max(prev+nums[i-1],nums[i-1])
            if prev==nums[i-1]:
                start=i
            maxx=max(maxx,prev)
            if maxx==prev:
                end=i
        print(start,end)
        return maxx
        