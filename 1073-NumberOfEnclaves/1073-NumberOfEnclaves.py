# Last updated: 5/6/2025, 11:06:34 pm
class Solution:
    def numEnclaves(self, board: List[List[int]]) -> int:
        def neighbour(cur):
            li=[]
            deltas=[(0,1),(0,-1),(1,0),(-1,0)]
            for d in deltas:
                newx,newy=(cur[0]+d[0],cur[1]+d[1])
                if newx>=0 and newx<m and newy>=0 and newy<n and\
                board[newx][newy]==1:
                    li.append((newx,newy))
            ##print(li)
            return li
        m=len(board)
        n=len(board[0])
        q=deque()
        #visited=set()
        for i in range(m):
            
                if board[i][0]==1:
                    q.append((i,0))
                    #visited.add((i,0))
                if board[i][n-1]==1:
                    q.append((i,n-1))
                    #visited.add((i,n-1))
        for j in range(n):
            if board[0][j]==1:
                q.append((0,j))
                #visited.add((0,j))
            if board[m-1][j]==1:
                q.append((m-1,j))
                #visited.add((m-1,j))
        #for each one call a dfs 
        
        
            
            
        
        
        while len(q)!=0:
            cur=q.popleft()
            
            
            #print(f'cur {cur}')
            
            
            board[cur[0]][cur[1]]=-1
            #visited.add(cur)
            for nei in neighbour(cur):
                
                    #if nei not in visited:
                        #print(f'nei  {nei}')
                        #visited.add(nei)
                        board[nei[0]][nei[1]]=-1
                        q.append(nei)
                    #board[nei[0]][nei[1]]='#'
            #print(visited,empty)
        #print(q)
        #multi_bfs(q,board)
        #print(board)
        count=0
        for i in range(m):
            for j in range(n):
                if board[i][j]==1:
                    count+=1
       
        return count