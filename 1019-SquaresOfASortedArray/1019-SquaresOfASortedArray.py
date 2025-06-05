# Last updated: 5/6/2025, 11:06:40 pm
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]
        nums.sort()
        return nums