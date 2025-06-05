# Last updated: 5/6/2025, 11:09:08 pm
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp=[0]*len(nums)
        dp[0]=nums[0],nums[0]
        maxx=dp[0][0]
        for i in range(1,len(nums)):
            dp[i]=max(dp[i-1][0]*nums[i],dp[i-1][1]*nums[i],nums[i]),min(dp[i-1][0]*nums[i],dp[i-1][1]*nums[i],nums[i])
            maxx=max(maxx,dp[i][0])
        return maxx