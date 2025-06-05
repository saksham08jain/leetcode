# Last updated: 5/6/2025, 11:07:31 pm
class Solution:
    def findDisappearedNumbers(self, nums):
        ans = []
        for c in nums:
            nums[abs(c)-1] = -abs(nums[abs(c)-1])
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
        return ans