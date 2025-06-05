# Last updated: 5/6/2025, 11:07:59 pm
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        coins.sort()
        for am in range(amount+1):
            for i in coins:
                if am-i<0:
                    break
                dp[am]=min(dp[am],dp[am-i]+1)
        print(dp[amount])
        if dp[amount]==float('inf'):
            return -1 
        else:
            return dp[amount]

