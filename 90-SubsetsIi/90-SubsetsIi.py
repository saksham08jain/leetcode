# Last updated: 5/6/2025, 11:09:53 pm
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        


        nums.sort()
        def helper(nums: List[int], index: int, current: List[int], res: List[List[int]]):
            res.append(current)
            prev=float('inf')
            for i in range(index, len(nums)):
                if nums[i]==prev:
                    continue
                prev=nums[i]
                helper(nums, i + 1, current + [nums[i]], res)
        
        res = []
        helper(nums, 0, [], res)
        return res


