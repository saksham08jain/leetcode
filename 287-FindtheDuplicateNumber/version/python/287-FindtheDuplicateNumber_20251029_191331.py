# Last updated: 29/10/2025, 19:13:31
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #okay in terms of indegree of a graph 
        #duplicate will have a indegree >=2
        
        ##floyd cycle detcection 
        slow=0
        fast=0 
        #intiially slow =fast 
        while 1:
            fast=nums[nums[fast]]
            slow=nums[slow]
            if slow==fast:
                break
        #now when they intersect 
        #reser one thing to 0 
        #say slow 
        slow=0 
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
        return slow 

        