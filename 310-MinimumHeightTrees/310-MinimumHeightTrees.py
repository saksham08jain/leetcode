# Last updated: 5/6/2025, 11:08:03 pm
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        adj=[[] for i in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        leaves=deque()
        edges_cnt=[-1]*n
        for i in range(n):
            if len(adj[i])==1:
                leaves.append(i)
            edges_cnt[i]=len(adj[i])

        while n>2:
           
            for _ in range(len(leaves)):
                leaf=leaves.popleft()
                n-=1 # remvoe the leaf  
                for neighbour in adj[leaf]:
                    edges_cnt[neighbour]-=1
                    if edges_cnt[neighbour]==1:
                        leaves.append(neighbour)
        return(list(leaves))