# Last updated: 24/11/2025, 09:36:10
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans=[] 
        prev=0
        for b in nums:
            cur=(prev<<1) | b
            if cur%5==0:
                ans.append(True)
            else: 
                ans.append(False)
            prev=cur
        return ans
            
        