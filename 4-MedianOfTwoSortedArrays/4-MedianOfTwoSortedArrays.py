# Last updated: 5/6/2025, 11:10:47 pm
from typing import *
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            return self.findMedianSortedArrays(nums2,nums1)
        left_ele=(len(nums1)+len(nums2)+1)//2
        lo=-1
        hi=len(nums1)-1
        #if hi is minus -1 , it means no element in nums1
        #implies median is the middle element of nums2
        # if hi==-1:
        #     if (len(nums1)+len(nums2))%2:
        #         return nums2[left_ele-1]
        #     else:
        #         return (nums2[left_ele-1]+nums2[left_ele])/2
        while hi>=lo:
            mid=(hi+lo)//2
            #picking mid elements from arr1 for initial partition 
            l1=mid 
            l2=left_ele-mid -2
            r1=l1+1
            r2=l2+1
            print('mid',mid)
            print('l1',l1)
            print('l2',l2)
            print('r1',r1)
            print('r2',r2)

            l1_ele,l2_ele=-float('inf'),-float('inf')
            r1_ele,r2_ele=float('inf'),float('inf')
            if l1>=0:
                l1_ele=nums1[l1]
            if l2>=0:
                l2_ele=nums2[l2]
            if r1<len(nums1):
                r1_ele=nums1[r1]
            if r2<len(nums2):
                r2_ele=nums2[r2]
                
            if l1_ele>r2_ele:
                hi=mid-1 
            elif l2_ele>r1_ele:
                lo=mid+1
            else:
                #correct picked , we can find median 
                if (len(nums1)+len(nums2))%2:
                    #odd length pick the middle element
                    median=max(l1_ele,l2_ele)
                else:
                    median=(
                            (max(l1_ele,l2_ele)
                             +min(r1_ele,r2_ele))
                            )/2
                return median