# Last updated: 5/6/2025, 11:10:44 pm
class Solution:
    def reverse(self, x: int) -> int:
        neg=False
        if x<0:
            x*=-1
            neg=True
        ans=(int(str(x)[::-1]))
        if ans<-(2**31) or ans>2**31-1:
            return 0
        if neg:
            return -ans
        return ans
        