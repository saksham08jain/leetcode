# Last updated: 5/6/2025, 11:10:30 pm
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        ptr=0
        index=1
        
        while(ptr<len(nums)):
            if nums[index-1]==nums[ptr]:
                ptr+=1
            else:
                nums[index]=nums[ptr]
                index+=1
                ptr+=1
        return index