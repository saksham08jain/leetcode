# Last updated: 5/6/2025, 11:10:26 pm
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def findMin():

            left, right = 0, len(nums) - 1

            while left < right:

                mid = (left + right) // 2

                if nums[mid] > nums[right]:

                    left = mid + 1

                else:

                    right = mid

            return left
        
        minidx=findMin()
        left=minidx
        n=len(nums)
        arr=nums
        right=minidx+n
        #print(minidx)
        
        while left<right:
            mid=(left+right)//2
            if arr[mid%n]==target:
                return mid%n
            elif arr[mid%n]>target:
                right=mid
            else:
                left=mid+1
            #print(left,mid,right)
            
        if arr[mid%n]==target:
            return mid%n
        else:
            return -1