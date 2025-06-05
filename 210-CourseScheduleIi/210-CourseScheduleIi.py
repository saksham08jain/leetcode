# Last updated: 5/6/2025, 11:08:40 pm
class Solution:
    def findOrder(self, numCourses: int,arr: List[List[int]]) -> List[int]:
        adj=[[] for i in range(numCourses)]
        
        def arr2adj():
            for u,v in arr:
                adj[u].append(v)
        colors=[0  for i in range(numCourses)]
        cycle=False
        order=[]
        def dfs(s):
            nonlocal cycle,order
            colors[s]=1 
            for neighbour in adj[s]:
                if colors[neighbour]==1:
                    cycle= True #there is a cyle 
                if colors[neighbour]==0:
                    dfs(neighbour)
            colors[s]=2
            order.append(s)
        def detect_cycle():
            for i in range(numCourses):
                #print(i,dfs(i))
                if colors[i]==0:
                    dfs(i)
                
                
            return cycle
        
        arr2adj()
        #print(adj)
        #print(cycle())
        detect_cycle()
        if cycle:
            return []
        return order