# Last updated: 21/11/2025, 09:23:44
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        gcd_, ans = gcd(a,b), 0

        for n in range(1, gcd_+1):

            if a%n ==0 and b%n==0:
                ans+=1
        return ans