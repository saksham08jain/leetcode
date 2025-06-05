# Last updated: 5/6/2025, 11:10:04 pm
class Solution:
    def climbStairs(self, n: int) -> int:
        #dp[i]=dp[i-2]+dp[i-1]
        #dp[0]=1 dp[-ve]=0 
        dp=[1]*(n+1)
        for i in range(1,n+1):
            dp[i]=dp[i-1]
            if i>1:
                dp[i]+=dp[i-2]
        return(dp[n])