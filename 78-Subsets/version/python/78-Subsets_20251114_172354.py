# Last updated: 14/11/2025, 17:23:54
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #2^n subsets 
        n=len(nums)
        start=0 
        end=1<<n
        ans=[]
        for num in range(start,end):
            sub=[]
            for i in range(n):
                if num&(1<<i):
                    sub.append(nums[i])
            ans.append(sub)
        return ans

        