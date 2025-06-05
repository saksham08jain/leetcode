# Last updated: 5/6/2025, 11:07:04 pm
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

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def dijkstra( V: int, adj: List[List[int]], S: int) -> List[int]:
        # Code here
            pq=MinHeap()
            pq.push((0,S))
            dist=[float('inf')]*(V+1)
            dist[S]=0
            while(len(pq)!=0):
                cur_dist,cur=pq.pop()
                #update distances to its neighbors 
                for nei,w in adj[cur]:
                    if dist[cur]+w<dist[nei]:
                        dist[nei]=w+dist[cur]
                        pq.push((dist[nei],nei))
            #print(*dist)
            return dist
        adj=[[] for i in range(n+1)]
        def arr2adj():
            for u,v,w in times:
                adj[u].append((v,w))
                
        arr2adj()
        if max(dijkstra(n,adj,k)[1:])==float('inf'):
            return -1 
        else:
            return max(dijkstra(n,adj,k)[1:])