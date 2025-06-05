# Last updated: 5/6/2025, 11:06:04 pm
class Solution:
    def countFairPairs(self, arr: List[int], lower: int, upper: int) -> int:
        n=len(arr)
        arr.sort()
        ans=0
        for i in range(n):
            #fix the ith element
            
                
            
            lower_bound = lower-arr[i]
            upper_bound = upper-arr[i]
            
            lo = bisect.bisect_left(arr, lower_bound, i + 1, n)
            hi = bisect.bisect_right(arr, upper_bound, i + 1, n) - 1
            
            # Count valid pairs
            if lo <= hi:
                ans += hi - lo + 1
        return(ans)
            