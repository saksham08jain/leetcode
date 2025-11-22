# Last updated: 22/11/2025, 17:05:42
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans=0
        for x in nums:
            if x%3!=0:
                ans+=1 
        return ans
        