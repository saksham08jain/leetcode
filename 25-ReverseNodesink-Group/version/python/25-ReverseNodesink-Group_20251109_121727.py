# Last updated: 09/11/2025, 12:17:27
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        #okay now i have a list of heads 
        def reverse(head):
            #revreses a linked list and returns the new head
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
       
        dummy=ListNode()
        prevHead=dummy
        while head:
            cur=head
            prev=None
            i=k
            while i:
                i-=1 
                if not cur:
                    prevHead.next=head
                    return dummy.next
                prev=cur

                cur=cur.next 
            if prev:
                prev.next=None 
            prevHead.next=reverse(head)
            prevHead=head
            head=cur

        return dummy.next
