# Last updated: 5/6/2025, 11:10:05 pm
class Solution:
    def mySqrt(self, x: int) -> int:
        lo=0
        hi=(x)//2+1
        mid=(lo+hi+1)//2
        while(mid*mid!=x):
            if(lo==mid or hi==mid):
                return mid-1
            if(mid*mid>x):
                hi=mid
                
            else:
                lo=mid
            mid=(hi+lo+1)//2   
        return mid