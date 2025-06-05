# Last updated: 5/6/2025, 11:09:13 pm
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
        arr={}
        count=0
        cur=head
        while(cur):
            arr[count]=cur
            cur=cur.next
            count+=1 

        i=0 
        j=count-1

        while(i<j-1):
            #print(i,j)
            arr[i].next=arr[j]
            arr[j].next=arr[i+1]
            
            arr[j-1].next=None
            i+=1
            j-=1

        return head