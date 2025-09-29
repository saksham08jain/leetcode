# Last updated: 29/09/2025, 13:41:16
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        lo=1
        hi=max(piles)
        ans=-1
        def check(mid):
            t=0
            for i in range(n):
                t+=(piles[i])//mid 
                if piles[i]%mid!=0:
                    t+=1
            return t<=h

        while hi>=lo:
            mid=(lo+hi)//2
            # print(mid,check(mid))
            if check(mid):
                # with k eating speed koko was able to eat 
                # try decreasing speed 
                hi=mid-1 
                ans=mid
            else:
                lo=mid+1
        return ans

