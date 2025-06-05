# Last updated: 5/6/2025, 11:06:18 pm
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

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m=len(heights)
        n=len(heights[0])
        def get_neighbours(cur):
            x=cur[0]
            y=cur[1]
            dx=[1,0,-1,0]
            dy=[0,-1,0,1]
            nei_li=[]
            for i in range(4):
                newx=x+dx[i]
                newy=y+dy[i]
                if newx>=0 and newx<=m-1 and newy>=0 and newy<=n-1:
                    nei_li.append((newx,newy)) 
            return nei_li
    # Code here
        pq=MinHeap()
        S=(0,0)
        pq.push((0,S))
        dist=[[float('inf')]*n for i in range(m)]
        dist[S[0]][S[1]]=0
        while(len(pq)!=0):
            cur_dist,cur=pq.pop()
            #update distances to its neighbors 
            for nei in get_neighbours(cur):
                w=abs(heights[nei[0]][nei[1]]-heights[cur[0]][cur[1]])
                if max(dist[cur[0]][cur[1]],w)<dist[nei[0]][nei[1]]:
                    dist[nei[0]][nei[1]]=max(dist[cur[0]][cur[1]],w)
                    pq.push((dist[nei[0]][nei[1]],nei))
        #print(*dist)
        return dist[m-1][n-1]

    
        