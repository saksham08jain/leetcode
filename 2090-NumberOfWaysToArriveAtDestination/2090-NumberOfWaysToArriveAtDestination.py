# Last updated: 5/6/2025, 11:06:10 pm
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
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod=10**9+7
        adj=[[] for i in range(n)]
        for u,v,w in roads:
            
            adj[u].append((v,w))
            adj[v].append((u,w))
        pq=MinHeap([])
        pq.push((0,0))
        dist=[float('inf')]*n
        dist[0]=0
        ways=[0]*n
        ways[0]=1
        while(len(pq)!=0):
            cur_dist,cur=pq.pop()
            #update distances to its neighbors 
            for nei,w in adj[cur]:
                if cur_dist+w<dist[nei]:
                    dist[nei]=w+cur_dist
                    ways[nei]=ways[cur]
                    pq.push((dist[nei],nei))
                elif cur_dist+w==dist[nei]:
                    ways[nei]=(ways[nei]+ways[cur])%mod
        #print(*dist)
        return ways[n-1]