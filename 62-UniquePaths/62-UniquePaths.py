# Last updated: 5/6/2025, 11:10:07 pm
class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0 if i!=m-1 else 1 for i in range(m)] for j in range(n)]
        dp[n-1]=[1 for i in range(m)]
        #print(dp)
        for i in range(n-2,-1,-1):
            for j in range(m-2,-1,-1):
                #print(i,j)
                dp[i][j]=dp[i+1][j]+dp[i][j+1]
        return dp[0][0]
        '''
        memo={}
        memo[0]=1
        memo[1]=1
        def fact(x):
            if x in memo:
                return memo[x]
            memo[x]=x*fact(x-1)
            return memo[x]
        return fact(m+n-2)//(fact(m-1)*fact(n-1))
        '''