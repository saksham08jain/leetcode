# Last updated: 5/6/2025, 11:06:06 pm
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len=-1 
        cur_len=0 
        maxx=max(nums)
        n=len(nums)
        for i in range(n):
            if nums[i]&maxx==maxx:
                cur_len+=1 
            else:
                max_len=max(max_len,cur_len)
                cur_len=0
        max_len=max(max_len,cur_len)
        return max_len
        