# Last updated: 5/6/2025, 11:09:22 pm
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node==None:
            return None
        newnode=Node(node.val,[])
        copied={}
        copied[node.val]=newnode
        queue=[]

        queue.append(node)

        while(len(queue)!=0):
            curr=queue.pop(0)
            #print(curr.val)
            newcurr=copied[curr.val]
            for nei in curr.neighbors:

                if nei.val not in copied:

                    temp=Node(nei.val,[])
                    queue.append(nei)    
                    copied[nei.val]=temp

                newcurr.neighbors.append(copied[nei.val])

                
        return newnode