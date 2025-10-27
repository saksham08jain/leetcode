# Last updated: 27/10/2025, 09:15:43
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans=ListNode()
        carry=0
        cur=ans
        def getval(ptr):
            if ptr==None:
                return 0 
            return ptr.val 
        def get_next(ptr):
            if ptr==None:
                return None
            return ptr.next
        ptr1=l1 
        ptr2=l2
        while ptr1 or ptr2:
           
            cur.next=ListNode((getval(ptr1)+getval(ptr2)+carry)%10)
            carry=(getval(ptr1)+getval(ptr2)+carry)//10
            ptr1=get_next(ptr1)
            ptr2=get_next(ptr2)
            cur=cur.next
        if carry:
            cur.next=ListNode(carry)
        ans=ans.next 
        return ans