# Last updated: 05/10/2025, 23:16:55
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
         
        #  keep a set and move pointers carefully 
        rolling_seen=set() 
        left=0 
        right=0 
        max_len=0
        n=len(s)
        while right<n:
            
            while s[right] in rolling_seen: #if i have seen the right pointer in the rolling seen i have to move left pointer until everything become unique 
                rolling_seen.remove(s[left])
                left+=1 
            max_len=max(right-left+1,max_len)
            rolling_seen.add(s[right])
            right+=1 
        return max_len