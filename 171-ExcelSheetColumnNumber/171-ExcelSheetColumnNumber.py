# Last updated: 5/6/2025, 11:09:01 pm
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col=0
        for j in range(len(columnTitle)):
            col+=(ord(columnTitle[j])-ord("A")+1)*26**(len(columnTitle)-j-1)
            
        return col