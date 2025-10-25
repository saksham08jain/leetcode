# Last updated: 25/10/2025, 19:05:36
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1=list1 
        ptr2=list2 
        head=ListNode() 

        #if one list is offer never pick elements from it which means return infinity 
        def get_ele(node):
            if node==None: 
                return float('inf')
            return node.val
        def get_next_node(node):
            if node==None:
                return node 
            return node.next 
        cur=head
        while(ptr1!=None or ptr2!=None):#if any element is remaining 


            #check which element is smaller 
            if get_ele(ptr1)<=get_ele(ptr2):
                #ptr1 is smaller 
                cur.next=ptr1 
                ptr1=get_next_node(ptr1)

            else:
                cur.next=ptr2 
                ptr2=get_next_node(ptr2)
            cur=cur.next 


        head=head.next 
        return head 
        