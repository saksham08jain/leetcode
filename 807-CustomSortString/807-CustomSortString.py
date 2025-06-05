# Last updated: 5/6/2025, 11:06:55 pm
from collections import defaultdict
class Solution:
    
    def customSortString(self, order: str, s: str) -> str:
        slist=sorted(s)
        priority=0
        def deff():
            return 27
        pmap=defaultdict(deff)
        for i in order:
            pmap[i]=priority
            priority+=1
        #print(pmap)
        
        def agb(a):
            return pmap[a]
        
        slist.sort(key=agb)
        return ''.join(slist)