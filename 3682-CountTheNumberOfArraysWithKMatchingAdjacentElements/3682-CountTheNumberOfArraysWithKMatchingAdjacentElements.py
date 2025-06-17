# Last updated: 17/6/2025, 5:45:06 pm
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        mod=10**9+7
        def nCr(n, r):
            if r < 0 or r > n:
                return 0
            res = 1
            for i in range(1, r + 1):
                res = res * (n - r + i) % mod
                res = res * pow(i, mod - 2, mod) % mod  # Modular inverse of i
            return res
        ans=nCr(n-1,k)
        ans*=m
        ans%=mod
        for i in range(n-k-1):
            ans*=(m-1)
            ans%=mod 
        return(ans)