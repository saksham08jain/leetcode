# Last updated: 5/6/2025, 11:06:37 pm
from typing import * 
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #multi source bfs 
        #for each orange time taken to rot will be min of time 
        #from all sources 

        #dummy node??
        m=len(grid)
        n=len(grid[0])

        q=deque()
        empty=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append(((i,j),0))
                if grid[i][j]==0:
                    empty+=1
        #print(time)
        #print(q)
        
        def multi_bfs(q):
            t=0
            def neighbour(cur):
                li=[]
                deltas=[(0,1),(0,-1),(1,0),(-1,0)]
                for d in deltas:
                    nei=(cur[0]+d[0],cur[1]+d[1])
                    if nei[0]>=0 and nei[0]<m and nei[1]>=0 and nei[1]<n\
                    and grid[nei[0]][nei[1]]==1:
                        li.append(nei)
                #print(li)
                return li
            visited=set()
            while len(q)!=0:
                cur=q.popleft()
                #print(f'cur {cur}')
                t=cur[1]
                cur=cur[0]
                
                visited.add(cur)
                for nei in neighbour(cur):
                    if nei not in visited:
                        #print(f'nei  {nei}')
                        visited.add(nei)
                        q.append((nei,t+1))
            #print(visited,empty)
            if len(visited)!=m*n-empty:
                return -1
            return t
        return multi_bfs(q)