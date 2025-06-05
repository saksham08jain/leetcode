# Last updated: 5/6/2025, 11:09:58 pm
class Solution:
    def subsets(self, nums: List[int]):
        self.all_subs=[]
        return self.helper(nums)
    def helper(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums)==0:
            self.all_subs.append( [])
            return [[]]

        for subset in self.helper(nums[1:]):
            copy=subset[:]
            copy.append(nums[0])
            self.all_subs.append(copy)
        return self.all_subs[:]