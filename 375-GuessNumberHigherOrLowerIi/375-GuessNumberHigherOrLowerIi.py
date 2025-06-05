# Last updated: 5/6/2025, 11:07:47 pm
#tabulation
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        ans=float('inf')
        memo={}
        def solve():
            #nonlocal ans
            def getmemo(start,end):
                if start==end:
                    return 0
                if end<=0 or start>=n or end<start:
                    return 0
                if (start,end) in memo:
                    return memo[(start,end)]
            
            for start in range(n,0,-1):
                for end in range(start,n+1):
                    minn=float('inf')
                    maxx=-1
            
                    for i in range(start,end):
                        maxx=max(
                                    getmemo(start,i-1),getmemo(i+1,end)
                                    )
                        minn=min(minn,
                                i+
                                maxx
                                )
                    if minn==float('inf'):
                        memo[(start,end)]=0
                    else:    
                        memo[(start,end)]=minn

                
        solve()
        #print(memo)
        return memo[(1,n)]
#Memoization solutions 
'''
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        ans=float('inf')
        memo={}
        def solve(start,end):
            #nonlocal ans

            if start==end:
                return 0
            if end<=0 or start>=n or end<start:
                return 0
            if (start,end) in memo:
                return memo[(start,end)]
            maxx=-1
            minn=float('inf')
            for i in range(start,end):
                maxx=max(
                            solve(start,i-1),solve(i+1,end)
                             )
                minn=min(minn,
                        i+
                        maxx
                        )
                #print(f'{start} to {end} {maxx}')
            memo[(start,end)]=minn
                #minn=min(minn,maxx)
            return minn
        maxx=solve(1,n)
        return maxx
'''