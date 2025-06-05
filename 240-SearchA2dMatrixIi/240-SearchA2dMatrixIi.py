# Last updated: 5/6/2025, 11:08:18 pm
from bisect import bisect_right
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bisect_right(arr,target):
            lo=0
            hi=len(arr)-1
            while(lo<=hi):
                mid=(lo+hi)//2
                if arr[mid]<=target:
                    lo=mid+1
                else:
                    hi=mid-1
            return lo
        first_col=[]
        m=len(matrix)
        for j in range(m):
            first_col.append(matrix[j][0])

        imax=bisect_right(first_col,target)
        
        for i in range(imax):
            idx=bisect_right(matrix[i],target)
            if matrix[i][idx-1]==target:
                return True
           
        return False