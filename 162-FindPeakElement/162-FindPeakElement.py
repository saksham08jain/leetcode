# Last updated: 5/6/2025, 11:09:04 pm
class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
       
        l = 0
        r = len(arr)-1
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l