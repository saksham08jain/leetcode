# Last updated: 5/6/2025, 11:07:38 pm
def findPages(arr: [int], n: int, m: int) -> int:

    # Write your code here
    # Return the minimum number of pages
    pass

class Solution:
    def splitArray(self, arr: List[int], k: int) -> int:
        n=len(arr)
        m=k
        if m>n:
            return -1
        if m==n:
            return max(arr)
        def check(maxx):
            cur=0 
            blocks=1
            for i in range(n):
                cur+=arr[i]
                if cur>maxx:
                    cur=arr[i]
                    blocks+=1
            return blocks<=m 
        #print(check(-1),check(0),check(1))
        lo=max(arr)
        hi=sum(arr)
        ans=-1
        while hi>=lo:
            mid=(hi+lo)//2
            #print(mid,check(mid))
            if check(mid):
                hi=mid-1
                ans=mid
            else:
                lo=mid+1
        
        #print('3',check(3))
        #print('4',check(4))
        return(ans)