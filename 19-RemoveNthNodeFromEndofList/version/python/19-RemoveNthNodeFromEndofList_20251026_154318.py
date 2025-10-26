# Last updated: 26/10/2025, 15:43:18
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #ah yes another one of the tricksters 
        #can do with space 
        #but there ezists a trick to do this without space 

        #good thing i have seen it before heheh 
        #have two nodes 
        #if i give one node a headstart of N 
        #by the time it reaches None 
        #the back node will be at N behind it 
        #and will be the node needing to be removed 
        #again no one thinks like this 

        #i can just find length  and find position of nth 
        #it is two pass though and i know i can implment it anyway lets just implment the trick 

        slow=head 
        fast=head 
        while(n):
            n-=1
            fast=fast.next 
        
        #what if fast is none here 
        #can only happen if trying to remove first elemnt of list
        #yup the slow.next.next logic collapses 

        if not fast:
            return head.next
        while fast.next!=None:
            slow=slow.next 
            fast=fast.next 
        #once fast is None  
        #we know which node to remove 

        print(slow.val)
        slow.next=slow.next.next 

        return head