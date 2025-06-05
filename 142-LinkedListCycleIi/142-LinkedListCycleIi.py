# Last updated: 5/6/2025, 11:09:14 pm
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #dumhead=ListNode(-1,head)
        #turt=dumhead
        #hare=dumhead
        turt=head
        if(turt==None):
            return None
        hare=head
        first=True
        while(first or turt!=hare):
            first=False
            turt=turt.next
            if(hare==None or hare.next==None):
                return None
            hare=hare.next.next

        #now turt=hare ie both are at k-x inside the cycle 
        print(turt.val)
        hare=head
        while(turt!=hare):
            turt=turt.next
            hare=hare.next
        print(turt.val)
        return turt