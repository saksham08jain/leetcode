# Last updated: 5/6/2025, 11:07:57 pm
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #think about constraints later 
        if head==None:
            return head
        odd=head 
        evenhead=head.next 
        even=evenhead

        while(even!=None):
            #print(odd.val,even.val)
            odd.next=even.next
            if(odd.next==None):
                odd.next=evenhead
                break
            odd=odd.next
            even.next=odd.next
            even=even.next
            
            
        odd.next=evenhead
        return head
