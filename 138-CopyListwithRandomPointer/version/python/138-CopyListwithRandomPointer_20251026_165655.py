# Last updated: 26/10/2025, 16:56:55
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #okay lets go 
        #lets copy the list without randoms 
        new_head=ListNode() 
        #stub head 
        cur=head 
        copy_cur=new_head
        nodes_list=[]
        while cur:
            copy_cur.next=ListNode(cur.val)
            
            copy_cur=copy_cur.next
            nodes_list.append(copy_cur)
            cur=cur.next 
        nodes_list.append(None)

        #copied 
        #now i will add random pointers 
        #how?
        #i need index of ranomd pointers in original list 
        #let me get those indeexes 
        indexes_list=[]
        cur=head

        while cur!=None:
            i=0
            temp=head 
            while temp is not cur.random:
                temp=temp.next
                i+=1
            #now temp is cur.ranomd 
            indexes_list.append(i)
            cur=cur.next
        #i should have gotten this correct for every element in the list 
        for i in range(len(indexes_list)):
            nodes_list[i].random=nodes_list[indexes_list[i]]
        
        return nodes_list[0]
