# Last updated: 5/6/2025, 11:06:54 pm
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        color = [0] * V  # 0 = unvisited, 1 = visiting, 2 = safe
        
        # DFS to detect cycles and mark safe nodes
        def dfs(node):
            if color[node] != 0:  # If already processed
                return color[node] == 2  # Return True if it's safe
            
            color[node] = 1  # Mark as visiting (part of current stack)
            
            for neighbor in graph[node]:
                if color[neighbor] == 2:  # Already known to be safe
                    continue
                if color[neighbor] == 1 or not dfs(neighbor):  # Cycle detected or unsafe
                    return False
            
            color[node] = 2  # Mark as safe
            return True
        
        safe_nodes = []
        for i in range(V):
            if dfs(i):  # If the node is safe, add it to the list
                safe_nodes.append(i)
        
        return sorted(safe_nodes)
