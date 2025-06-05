# Last updated: 5/6/2025, 11:06:57 pm
from typing import List
from heapq import *
class MinHeap:
    def __init__(self,arr=[]):
        self.heap=arr
        heapify(self.heap)
    def push(self,ele):
        heappush(self.heap,ele)
    def pop(self):
        return heappop(self.heap) 
    def __len__(self):
        return len(self.heap)
    def __str__(self):
        return str(self.heap)
class Solution:
    def findCheapestPrice(self, n: int,edges: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=[[] for i in range(n)]
        def arr2adj():
            for u,v,w in edges:
                adj[u].append((v,w))
                
        arr2adj()
        q=deque()
        q.append((0,0,src))
        dist=[float('inf')]*n
        dist[src]=0
        while(len(q)!=0):
            cur_stops,cur_dist,cur=q.popleft()
            print(cur,cur_dist,cur_stops)
            #update distances to its neighbors 
            for nei,w in adj[cur]:
                if cur_dist+w<dist[nei] and cur_stops<=k:
                    dist[nei]=w+cur_dist
                    q.append((cur_stops+1,dist[nei],nei))
        print(*dist)
        if dist[dst]==float('inf'):
            return -1
        return dist[dst]