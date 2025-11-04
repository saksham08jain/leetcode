# Last updated: 04/11/2025, 08:38:38
class Node:
    def __init__(self,key=None,val=None,next=None,prev=None):
        self.val=val
        self.next=next
        self.prev=prev
        self.key=key
    
class LRUCache:

    def __init__(self, capacity: int):
        #we will use a doubly linked list 
        #thought process is like 
        # we  want to keep our lsit or whatever data structure we would have wanted in order ie 
        #soretd by timestamp kinda thing 
        #so a deque was kinda natural progerssoni of that thought 
        # but we would want anything to move to right end 
        #hence we end up with dll
        self.capacity=capacity 
        #i amma add dummy head and tail since pretty sure down the line edge case will happen 
        self.left=Node()
        self.right=Node()
        self.left.next=self.right 
        self.right.prev=self.left

        #oh also id want direct pointers to every node 
        #except head and tail sicne i have those pointers alrady 
        self.map={}
         
    def _delete(self,ptr):
        #deletes the ptr and isolates it returns the isolated ptr 
        ptr.prev.next=ptr.next
        ptr.next.prev=ptr.prev
        ptr.next=None
        ptr.prev=None
        return ptr 
    def _insert(self,ptr):
        #inserts given isolated ptr at the right 
        ptr.next=self.right 
        temp=self.right.prev
        self.right.prev=ptr
        temp.next=ptr
        ptr.prev=temp 
        return ptr 


    def get(self, key: int) -> int:
        #get the value of something ... 
        ptr=self.map.get(key,None)
        if ptr is None:
            return -1 
        #otherwise return the value at ptr 
        #since this key was accessed move it to right 
        #rightmost = recently accessed 

        #ptr is now isolated 
        #add it to end 
        self._delete(ptr)
        self._insert(ptr)
        return ptr.val 

        

    def put(self, key: int, value: int) -> None:
        #if the key exists 
        #update value 
        if key in self.map:
            ptr=self.map.get(key)
            ptr.val=value 
            self._delete(ptr)
            #ptr is now isolated 
            #add it to end 
            self._insert(ptr)

        else:
            #the key doesnt exist 
            #we need to insert at right
            ptr=Node()
            ptr.val=value
            ptr.key=key
            self._insert(ptr) 
            self.map[key]=ptr
            
            if len(self.map)>self.capacity:
                del self.map[self.left.next.key]
                self._delete(self.left.next)
                
            
            

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)