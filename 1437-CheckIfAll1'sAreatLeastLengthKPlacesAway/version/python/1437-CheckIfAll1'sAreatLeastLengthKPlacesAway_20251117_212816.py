# Last updated: 17/11/2025, 21:28:16
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_one=-float('inf')
        for i in range(len(nums)):
            num=nums[i] 
            if num==1:
                if i-last_one<=k:
                    return False
                last_one=i 
        return True 
        