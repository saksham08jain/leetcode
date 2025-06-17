# Last updated: 17/6/2025, 5:45:14 pm
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        #nlogn via ordered set 
        # n square brute force 
        #giing brute force right now , maybe ordered set someday but python doesnthave an inbuilt ordered set oh well 
        n=len(nums)
        max_diff=0
        for i in range(n):
            for j in range(i+1,n):
                max_diff=max(nums[j]-nums[i],max_diff)
        return -1 if max_diff==0 else max_diff