# Last updated: 25/11/2025, 20:53:13
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        x=1 
        seen=set()
        seen.add(1)
        count=1
        while x%k:
            
            x=x*(10%k)+1
            x=x%k
            if x in seen: 
                return -1 
            count+=1
            seen.add(x)
        return count
