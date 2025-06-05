# Last updated: 5/6/2025, 11:08:55 pm
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*(n+4)
        for i in range(n-1,-1,-1):
            dp[i]=max(dp[i+1],dp[i+2]+nums[i])
        return dp[0]
        