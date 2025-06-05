# Last updated: 5/6/2025, 11:10:08 pm
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def length(head):
            ans=0
            cur=head       
            while(cur!=None):
                ans+=1
                cur=cur.next
            return ans 

        n=length(head)
        if(n==0):
            return None 
        k=k%n
        #seacrh for n-kth node 
        ans=0
        cur=head       
        while(cur!=None):
            ans+=1
            if(ans==n-k):
                prev=cur
                print(n,k,cur.val)
                break
            cur=cur.next
        end=prev
        while(end.next!=None):
            end=end.next
        #print(prev,end)
        end.next=head
        head=prev.next
        prev.next=None
        

        return head