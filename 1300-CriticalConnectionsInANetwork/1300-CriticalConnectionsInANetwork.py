# Last updated: 5/6/2025, 11:06:31 pm

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        adj = [[] for _ in range(n)]  # adjacency list
        
        # Step 1: Build adjacency list and track edges
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        time=0
        bridges=[]
        def dfs_timer(node,parent,times,lows):
                nonlocal time
                times[node] = time
                lows[node]=time
                for neighbor in adj[node]:
                    if times[neighbor]==-1:
                        time+=1
                        dfs_timer(neighbor,node,times,lows)
                    if neighbor!=parent:
                        lows[node]=min(lows[node],lows[neighbor])
                        #if lows[neighbor] > times[node]:
                        #    bridges.append([node, neighbor])
                if lows[node]>times[parent]: # not lows[node]>lows[parent]
                
                    bridges.append((parent,node))
        times = [-1] * n
        lows=[-1]*n
        for i in range(n):
            if times[i]==-1:
                dfs_timer(i,-1,times,lows)
        print(times)
        print(lows)
        return bridges
'''
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        adj = [[] for _ in range(n)]  # adjacency list
        
        # Step 1: Build adjacency list
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        
        time = 0
        bridges = []
        
        def dfs_timer(node, parent, times, lows):
            nonlocal time
            times[node] = time
            lows[node] = time
            time += 1
            
            for neighbor in adj[node]:
                if neighbor == parent:  # Don't go back to the parent
                    continue
                
                if times[neighbor] == -1:  # If neighbor is not visited
                    dfs_timer(neighbor, node, times, lows)
                    lows[node] = min(lows[node], lows[neighbor])
                    
                    # Check if the edge (node, neighbor) is a bridge
                    if lows[neighbor] > times[node]:
                        bridges.append([node, neighbor])
                else:
                    # Update lows[node] because neighbor was already visited
                    lows[node] = min(lows[node], times[neighbor])
        
        times = [-1] * n  # Discovery times of visited nodes
        lows = [float('inf')] * n  # Lowest discovery times reachable
        
        for i in range(n):
            if times[i] == -1:  # If the node has not been visited
                dfs_timer(i, -1, times, lows)
        
        return bridges
'''