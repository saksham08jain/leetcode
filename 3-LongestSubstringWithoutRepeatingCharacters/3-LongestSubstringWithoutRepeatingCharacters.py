# Last updated: 5/6/2025, 11:10:48 pm
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left, ans = 0, 0

        for right in range(len(s)):
            # Shrink the window from the left if a duplicate character is found
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            # Add the current character to the set and update the answer
            seen.add(s[right])
            ans = max(ans, right - left + 1)

        return ans
