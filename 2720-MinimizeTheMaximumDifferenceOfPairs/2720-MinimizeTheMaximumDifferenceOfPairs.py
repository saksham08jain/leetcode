# Last updated: 13/6/2025, 5:45:29 pm
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def check(d):
            #checks if i can find p pairs with difference less yhan eqial to d in the array 
            ptr=0 
            pairs=0 
            while ptr<n-1 :
                diff=sorted_arr[ptr+1]-sorted_arr[ptr]
                if abs(diff)<=d: #abs is redundat , array is sorted 
                    ptr+=2
                    pairs+=1
                else:
                    ptr+=1
                if pairs>=p:
                    return True 
            return False
        sorted_arr=sorted(nums)
        n=len(nums)
        lo=0#mind=0 
        hi=sorted_arr[-1]-sorted_arr[0]#maxd=arr[-1]-arr[0]
        ans=0
        while hi>=lo:
            mid=(hi+lo)//2
            if check(mid):
                ans=mid
                hi=mid-1
            else:
                lo=mid+1
        return ans