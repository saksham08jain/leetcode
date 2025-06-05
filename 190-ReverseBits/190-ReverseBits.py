# Last updated: 5/6/2025, 11:08:58 pm
class Solution:
    def reverseBits(self, n: int) -> int:
        ans=0
        index=0
        while(n):
            bit=n&1
            #print(bit)
            n//=2
            if(bit):
                ans+=1<<(31-index)
            index+=1
        return ans