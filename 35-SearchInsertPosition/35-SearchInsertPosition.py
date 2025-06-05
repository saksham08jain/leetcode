# Last updated: 5/6/2025, 11:10:25 pm
class Solution:
    def searchInsert(self, arr: List[int], target: int) -> int:
        def ubbinary():
            lo=-1
            hi=len(arr)
            
            mid=lo+(hi-lo)//2
            while(lo!=mid):
                
                #print(lo,mid,hi)
                #print(arr[mid])
                if arr[mid]==target:
                    return mid
                elif arr[mid]>target:
                    hi=mid 
                else:
                    #print('else block')
                    lo=mid 
                mid=lo+(hi-lo)//2
            return lo+1
        return ubbinary()