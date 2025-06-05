# Last updated: 5/6/2025, 11:08:56 pm
class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while(n):
            print(n)
            if n&1:
                count+=1
            n=n>>1
        return count