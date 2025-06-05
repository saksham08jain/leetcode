# Last updated: 5/6/2025, 11:07:51 pm
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        nums1ptr=0
        nums2ptr=0
        newarr=[]
        while(nums1ptr<len(nums1) and nums2ptr<len(nums2)):
            if(nums1[nums1ptr]==nums2[nums2ptr]):
                newarr.append(nums1[nums1ptr])
                nums1ptr+=1
                nums2ptr+=1
            elif nums1[nums1ptr]>nums2[nums2ptr]:
                nums2ptr+=1
            else:
                nums1ptr+=1
        return newarr