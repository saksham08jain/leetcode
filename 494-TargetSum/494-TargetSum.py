# Last updated: 5/6/2025, 11:07:26 pm
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n=len(nums)
        dp=[[-1 for j in range(2001)] for i in range(n)]
        
        def targetSum(index,target):
            
            
            
            
            if index>=n:
                return  target==0
            #print(index,target)
            if dp[index][abs(target)]!=-1:
                return dp[index][abs(target)]
            cur=nums[index]
            plussign=targetSum(index+1,abs(target-cur))
            minussign=targetSum(index+1,abs(target+cur))
            ans=plussign+minussign
            dp[index][abs(target)]=ans
            return ans
        return targetSum(0,abs(target))