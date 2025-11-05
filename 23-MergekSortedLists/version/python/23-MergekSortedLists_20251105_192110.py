# Last updated: 05/11/2025, 19:21:10
from heapq import heapify, heappush, heappop

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Create list of tuples for all non-empty list heads
        heap = []
        for i, node in enumerate(lists):
            if node:
                heap.append((node.val, i, node))
        
        # Heapify in O(k) time instead of O(k log k) with repeated heappush
        heapify(heap)
        
        dummy = ListNode()
        current = dummy
        counter = len(lists)
        
        while heap:
            val, idx, node = heappop(heap)
            current.next = node
            current = current.next
            
            if node.next:
                heappush(heap, (node.next.val, counter, node.next))
                counter += 1
        
        return dummy.next
# # # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# #     def __lt__(self,other):
# #         #probably __lt__ overwirte doesnt work i letteocde hmm 
# #         return self.val<other.val
# from heapq import * 
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         #Note detsroys input lists and changes ordering of input lists 
#         #it is easy to change it to duplicate the Node's value instead of detsryoing 

#         #just get the minimum and move it so simple 
#         #is this supposed to be hard? 
#         n=len(lists)
#         def get_next(ptr):
#             if ptr:
#                 return ptr.next
#             return None 
#         def get_val(ptr):
#             if ptr==None:
#                 return float('inf')
#             return ptr.val 
#         ans=ListNode()
#         ptr=ans
#         # new_lists=[(x.val,x) for x in lists]
#         # heapify(new_lists)
#         # mehh heapify without key is irritating me i amma go heappush, f it extra log k factor but i am fine 
#         new_lists=[] 
#         for x in range(n):
#             node=lists[x]
#             new_lists.append((node.val,x,node))
#         #lists is a lists of current pointers 
#         heapify(new_lists)
#         while 1:
            
#             #can i make this fasterr?? 
#             #howw? 
#             #well only one number is new from the last time i found the min ie only one ptr moved right 
#             #then why i am going through every number 
#             #Requirements 
#             #INsert at soretd order 
#             #access element with minimum value 
#             #Data Structure : Heap 
#             #you dont throw data strcuture to problems you match requirements 
#             #just the initial state is a bit confusing 


#             # for i in range(n):
#             #     cur=lists[i] 
#             #     if get_val(cur)<minn:
#             #         minn=get_val(cur)
#             #         min_idx=i
            
#             # if min_idx==-1:
#             #     break
#                 #get which pointer is minimum 
#             #move the minimum ptr to next 

            
#             _,_,temp=heappop(new_lists)
#             #i dont eve have a key function for heappop .. wtfff 
#             #gotta go tuple approach x.val,x ig but even then key wouldnt work since typles seoxcnd option is compared 
#             heappush(get_val(temp.next),get_next(new_lists[min_idx]))
#             temp.next=None
#             ptr.next=temp
#             ptr=ptr.next 
#         return ans.next 

#         # i will wirte a heap wrapper tonight ig 
