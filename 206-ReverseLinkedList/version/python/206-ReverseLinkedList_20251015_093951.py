# Last updated: 15/10/2025, 09:39:51
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        if head.next==None:
            return head
        cur=head.next 
        head.next=None 
        new_head=self.reverseList(cur)
        cur.next=head
        return new_head 

        
    
        