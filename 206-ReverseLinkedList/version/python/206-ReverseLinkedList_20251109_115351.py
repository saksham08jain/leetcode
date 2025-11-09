# Last updated: 09/11/2025, 11:53:51
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev=head 
        if not prev:
            return prev
        cur=head.next 
        prev.next=None

        if not cur:
            return prev 
        
        while cur!=None:
            nextt=cur.next
            cur.next=prev 
            prev=cur 
            cur=nextt 
        return prev
