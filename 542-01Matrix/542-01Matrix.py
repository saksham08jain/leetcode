# Last updated: 5/6/2025, 11:07:27 pm
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        def neighbour(cur):
            li=[]
            deltas=[(0,1),(0,-1),(1,0),(-1,0)]
            for d in deltas:
                newx,newy=(cur[0]+d[0],cur[1]+d[1])
                if newx>=0 and newx<m and newy>=0 and newy<n and\
                mat[newx][newy]==1:
                    li.append((newx,newy))
            #print(li)
            return li
        m=len(mat)
        n=len(mat[0])
        q=deque()
        new_mat=[[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.append(((i,j),0))
        #for each one call a dfs 
        
        def multi_bfs(q,new_mat):
            t=0
            
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
                        new_mat[nei[0]][nei[1]]=t+1
            #print(visited,empty)
            
        multi_bfs(q,new_mat)
        return new_mat