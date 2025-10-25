# Last updated: 25/10/2025, 19:24:41
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Turtle Hare method is one 
        #are there other algorithms too ? 
        ptr1=head
        ptr2=head 

        while(ptr1!=None and ptr2!=None):
            
            ptr1=ptr1.next 

            ptr2=ptr2.next 

            if(ptr2==None):
                return False 
            ptr2=ptr2.next
            if(ptr1==ptr2):
                return True
        return False
        