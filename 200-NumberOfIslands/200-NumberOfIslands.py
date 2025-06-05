# Last updated: 5/6/2025, 11:08:52 pm
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=[[False]*n for i in range(m)]

        def dfs_visit(i,j):
            #print(i,j)
            visited[i][j]=True 
            
            neighbours=[(min(i+1,m-1),j),(i,min(j+1,n-1)),(max(0,i-1),j),(i,max(0,j-1))]
            
            for (i,j) in neighbours:
                if not visited[i][j] and grid[i][j]=='1':
                    dfs_visit(i,j)
       
        num=0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j]=='1':
                    #print(i,j)
                    dfs_visit(i,j)
                    num+=1
        return num