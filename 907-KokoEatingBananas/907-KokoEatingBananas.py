# Last updated: 5/6/2025, 11:06:47 pm
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #bs on k 
        n=len(piles)
        def check(mid):
            #checks if this eating speed can eat all bananas
            if mid==0:
                return False
            time=0
            for i in range(n):
                time+=piles[i]//mid
                if piles[i]%mid:
                    time+=1
            return time<=h
        lo=0
        hi=max(piles)+1
        while hi>=lo:
            mid=(lo+hi)//2
            if check(mid):
                #try to reduce eating speed 
                hi=mid-1 
            else:
                lo=mid+1
        return(hi+1)