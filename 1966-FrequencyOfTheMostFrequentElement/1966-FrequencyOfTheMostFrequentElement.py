# Last updated: 5/6/2025, 11:06:13 pm
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        ans = 0
        curr = 0
        
        for right in range(len(nums)):
            target = nums[right]
            curr += target
            
            while (right - left + 1) * target - curr > k:
                curr -= nums[left]
                left += 1
            
            ans = max(ans, right - left + 1)

        return ans