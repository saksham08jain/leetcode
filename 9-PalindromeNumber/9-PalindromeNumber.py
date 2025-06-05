# Last updated: 5/6/2025, 11:10:42 pm
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]
        