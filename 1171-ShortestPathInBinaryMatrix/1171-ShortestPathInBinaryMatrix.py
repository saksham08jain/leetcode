# Last updated: 5/6/2025, 11:06:33 pm
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        dist=[[-1 for j in range(n)] for i in range(n)]
        def get_neighbours(cur):
            x=cur[0]
            y=cur[1]
            dx=[-1,-1,-1,0,0,1,1,1]
            dy=[-1,0,1,1,-1,-1,0,1]
            nei_li=[]
            for i in range(8):
                newx=x+dx[i]
                newy=y+dy[i]
                if newx>=0 and newx<=n-1 and newy>=0 and newy<=n-1\
                and grid[newx][newy]==0:
                    nei_li.append((newx,newy)) 
            return nei_li
        def bfs(i):
            q=deque()
            q.append(i)
            dist[i[0]][i[1]]=1
            while(len(q)!=0):
                #print(q,dist)
                cur=q.popleft()
                for nei in get_neighbours(cur):
                    if dist[nei[0]][nei[1]]==-1:
                        q.append(nei)
                        dist[nei[0]][nei[1]]=dist[cur[0]][cur[1]]+1
        if  grid[0][0]!=0:
            return -1
        bfs((0,0))
        return dist[n-1][n-1]
        