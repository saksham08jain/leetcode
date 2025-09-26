# Last updated: 26/09/2025, 09:54:39
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # treat the matrix as flat only
        lo=0 
        m=len(matrix)
        n=len(matrix[0])
        hi=m*n-1

        while hi>=lo:
            mid=(hi+lo)//2
            i=mid//n
            j=mid%n
            if matrix[i][j]>target:
                hi=mid-1
            elif matrix[i][j]<target:
                lo=mid+1
            else:
                return True 
        return False

        