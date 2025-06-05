# Last updated: 5/6/2025, 11:09:02 pm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            ele=nums[i]
            if count==0:
                guess=ele
            if ele!=guess:
                count-=1
            else:
                count+=1
        return guess