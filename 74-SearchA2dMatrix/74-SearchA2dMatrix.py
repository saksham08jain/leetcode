# Last updated: 5/6/2025, 11:10:01 pm
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo=0
        m=len(matrix)
        n=len(matrix[0])
        hi=m*n-1
        while(hi>=lo):
            mid=(hi+lo)//2
            midval=matrix[mid//n][mid%n]
            #print(lo,mid,hi,midval)
            if midval==target:
                return True 
            elif midval<target:
                lo=mid+1
            else:
                hi=mid-1
        return False