# Last updated: 5/6/2025, 11:09:19 pm
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        for i in nums:
            ans^=i
        return ans