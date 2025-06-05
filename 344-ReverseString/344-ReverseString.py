# Last updated: 5/6/2025, 11:07:53 pm
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i],s[len(s)-i-1]=s[len(s)-i-1],s[i]
            #print(s)