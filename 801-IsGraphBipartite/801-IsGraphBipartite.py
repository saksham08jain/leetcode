# Last updated: 5/6/2025, 11:06:58 pm
from collections import deque
from typing import List

class Solution:
    def isBipartite(self, adj: List[List[int]]) -> bool:
        v = len(adj)
        color = [-1] * v  # No need to store one extra element, as nodes are from 0 to v-1
        visited = [False] * v
        ans = True
        
        def bfs(node):
            nonlocal ans
            q = deque([node])
            visited[node] = True
            color[node] = 0  # Assign the starting node a color
            
            while q:
                cur = q.popleft()
                cur_color = color[cur]
                
                for nei in adj[cur]:
                    if color[nei] == -1:  # If the neighbor is uncolored
                        color[nei] = 1 - cur_color  # Assign opposite color
                        q.append(nei)
                        visited[nei] = True
                    elif color[nei] == cur_color:  # If the neighbor has the same color
                        ans = False
                        return
        
        # Check each component in case the graph is disconnected
        for i in range(v):
            if not visited[i]:
                bfs(i)
                if not ans:  # Early return if already found to be not bipartite
                    return False
        
        return True
