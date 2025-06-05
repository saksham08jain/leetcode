# Last updated: 5/6/2025, 11:10:32 pm
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dumhead=ListNode(-1,head)
        
        cur=dumhead
       

        while(cur!=None):
            after=cur.next
            if(cur.next==None or after.next==None):
                break
            cur.next=after.next
                
            after.next=cur.next.next
            cur.next.next=after
            cur=after
        #print(dumhead)
        return dumhead.next