# Last updated: 25/10/2025, 19:40:58
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #solution using memory ie O(n) is straight forward 
        #just store the insert elements and literally put them in between 

        #what if i dont wnat to use space 

        #doesnt seem to be a way to do so 
        #since the linked list only allows next not prev 

        #lets code the tsaright fowward solution then 

        slow=head 
        fast=head 
        to_insert=[] 

        while fast!=None:
            slow=slow.next 
            fast=fast.next 
            if(fast==None):
                break 
            fast=fast.next 

        mid=slow 
        cur=mid
        while cur!=None:
            to_insert.append(cur)
            cur=cur.next 
        
        cur=head
        while to_insert: 
            ins=to_insert.pop() 
            temp=cur.next 
            cur.next=ins 
            ins.next=temp 
            cur=cur.next.next 
        cur.next=None 
        return head

