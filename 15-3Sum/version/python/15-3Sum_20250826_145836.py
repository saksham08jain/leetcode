# Last updated: 26/08/2025, 14:58:36
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force is O(N3)
        # I can do sorting one iteration and then its basically two sum 
        # O(n log n + n**2)
        # can i do better than n sqaure 
        # can i keep three pointer but then how will I know which to move 
        # there was a dutch national flag algo though right what did it do?
        # is it related 
        # to make sure triplets arent repeated i can keep a set where i always put them in a sorted order 
        triplets=set() 
        n=len(nums)
        nums=sorted(nums)#this takes O(n) space since its a copy 
        for i in range(n):
            target=-nums[i]

            left=i+1 
            right=n-1 

            # standard two sum 
            while right>left and right>i:
                cur_sum=nums[right]+nums[left]
                if cur_sum==target:
                    # found one solution 
                    # print(target,left,right)
                    # we dont need sorting 
                    # nums[i],nums[left],nums[right] is already in soretd order
                    triplets.add(tuple(sorted([nums[i],nums[left],nums[right]])))
                    # aha yes cant use a set or list for triplets cause unhashable type wait i can use a tuple damnn
                    # what if there is more than one solution though 
                    # therefore move both 
                    # cause note triplets dont contain index but the number 
                    # Skip duplicates for left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for right pointer  
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    right-=1 
                    left+=1
                elif cur_sum<target:
                    left+=1 
                else:
                    right-=1
        return list(triplets)