# Last updated: 5/6/2025, 11:08:44 pm
class Solution:

    def canFinish(self, numCourses: int, arr: List[List[int]]) -> bool:
        #lets do 3 color dfs
        #first create adj list 
        adj=[[] for i in range(numCourses)]
        
        def arr2adj():
            for u,v in arr:
                adj[u].append(v)
        colors=[0  for i in range(numCourses)]
        cycle=False
        def dfs(s):
            nonlocal cycle
            colors[s]=1 
            for neighbour in adj[s]:
                if colors[neighbour]==1:
                    cycle= True #there is a cyle 
                if colors[neighbour]==0:
                    dfs(neighbour)
            colors[s]=2
            
        def detect_cycle():
            for i in range(numCourses):
                #print(i,dfs(i))
               
                dfs(i)
                
                
            return cycle
        
        arr2adj()
        #print(adj)
        #print(cycle())
        return not detect_cycle()

