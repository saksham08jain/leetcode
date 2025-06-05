# Last updated: 5/6/2025, 11:07:18 pm
from heapq import *

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
       #use heap , learn heap python 
       #max heap , default is minheap so negate the values 

        count={}
        for i in tasks:
            count[i]=count.get(i,0)+1
        
        count_heap=[-1 *i for i in count.values()]
        heapify(count_heap)
        steps=0
        while(len(count_heap)!=0):
            extracted=[]
            idlecount=0
            for i in range(n+1):
                
                if len(count_heap)==0:
                    idlecount+=1
                    steps+=1
                    continue
                max_count=heappop(count_heap)
                #print(steps,max_count)
                
                
                if max_count!=-1:    
                    
                    extracted.append(max_count)
                steps+=1
            for ext in extracted:
                
                heappush(count_heap,ext+1)
        return steps-idlecount



