# Last updated: 5/6/2025, 11:10:19 pm
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[False]*(n)

        dp[0]=True

        for idx in range(n):
            if not dp[idx]:
                continue
            for jump_len in range(1,nums[idx]+1):
                if idx+jump_len>=n:
                    dp[n-1]=True
                    return dp[n-1]
                
                else:
                    dp[idx+jump_len]=True
        print(dp)
        return dp[n-1]

