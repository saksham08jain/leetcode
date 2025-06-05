# Last updated: 5/6/2025, 11:09:11 pm
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Function to create a linked list from a list of values
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        def merge(head1,head2):
            ptr1=head1
            ptr2=head2 

            dumhead=ListNode(10**6)
            cur=dumhead

            while(ptr1 or ptr2):
                if ptr1==None:
                    val1=10**6
                else:
                    val1=ptr1.val
                if ptr2==None:
                    val2=10**6
                else:
                    val2=ptr2.val
                
                if val1>val2:
                    cur.next=ptr2
                    cur=cur.next 
                    ptr2=ptr2.next
                
                else:
                    cur.next=ptr1
                    cur=cur.next 
                    ptr1=ptr1.next
            return dumhead.next
        
        #find middle of the linked list 
        fast=head 
        slow=head 
        prev=head
        while(fast and fast.next):
            prev=slow
            slow=slow.next 
            fast=fast.next.next 
            

        mid=prev 
        second=mid.next
        mid.next=None
        first=head 

        #print(first.val,prev.val,mid.val)
        if first!=None and first.next!=None:
            l1=self.sortList(first)
        else:
            l1=first 
        if second!=None and second.next!=None :
            l2=self.sortList(second)
        else:
            l2=second

        return merge(l1,l2)