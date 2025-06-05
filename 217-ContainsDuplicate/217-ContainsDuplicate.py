# Last updated: 5/6/2025, 11:08:33 pm
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts={}
        for i in nums:
            if i in counts:
                counts[i]+=1
            else:
                counts[i]=1
            if counts[i]>=2:
                return True
        return False