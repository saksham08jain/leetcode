# Last updated: 5/6/2025, 11:10:49 pm
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dumhead=ListNode()
        carry=0
        ans=dumhead
        while(l1 or l2):
            if l1:
                val1=l1.val
                l1=l1.next
            else:
                val1=0
            if l2:
                val2=l2.val
                l2=l2.next
            else:
                val2=0
            ans.next=ListNode()
            ans=ans.next
            ans.val=(val1+val2+carry)%10
            
            carry=(val1+val2+carry)//10 
        if carry:
            ans.next=ListNode(carry)
        return dumhead.next
        
