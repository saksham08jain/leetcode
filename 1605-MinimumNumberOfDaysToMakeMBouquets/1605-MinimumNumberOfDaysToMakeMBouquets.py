# Last updated: 5/6/2025, 11:06:22 pm
class Solution:
    def minDays(self, bloomday: List[int], m: int, k: int) -> int:
        #bs on num_days 
        n=len(bloomday)
        def check(num_days):
            num_bqs=0 
            #i will count how many bqs can i make 
            #check with sliding window 
            i=0 
            start=-1
            while(i<n):
                #is i th flower bloomed
                if bloomday[i]<=num_days:
                    
                    if(i-start>=k):
                        
                        #print(start+1,i)
                        num_bqs+=1
                        start=i
                    i+=1
                else:
                    start=i
                    i+=1
            return num_bqs>=m
        
        lo=0 
        hi=max(bloomday)+1
        ans=-1
        while hi>=lo:
            mid=(hi+lo)//2
            if check(mid):
                hi=mid-1
                ans=mid
            else:
                lo=mid+1
        return ans
