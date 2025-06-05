# Last updated: 5/6/2025, 11:06:19 pm
class Solution:
    def maxDepth(self, s: str) -> int:
        open=0 
        close=0 
        max_depth=-1 
        for char in s:
            if char=='(':
                open+=1
            elif char==')':
                close+=1
            max_depth=max(max_depth,open-close)
        return max_depth