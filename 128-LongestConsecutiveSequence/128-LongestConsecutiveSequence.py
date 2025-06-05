# Last updated: 5/6/2025, 11:09:26 pm
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup=set(nums)
        ans=0
        for i in nums:
            if i not in lookup:
                continue
            x=i
            curans=1
            while x+1 in lookup:
                curans+=1
                
                lookup.remove(x+1)  
                x+=1
            x=i
            while x-1 in lookup:
                curans+=1
                lookup.remove(x-1)
                x-=1
            #print(i,curans)
            ans=max(ans,curans)
        return ans