# Last updated: 5/6/2025, 11:09:25 pm
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #what i have done is not in place 

        #bfs from 'Os' on the edge of board , store all 'Os' they could 
        #visit , new boardrix those are 'O's rest are 'X's
        def neighbour(cur):
            li=[]
            deltas=[(0,1),(0,-1),(1,0),(-1,0)]
            for d in deltas:
                newx,newy=(cur[0]+d[0],cur[1]+d[1])
                if newx>=0 and newx<m and newy>=0 and newy<n and\
                board[newx][newy]=="O":
                    li.append((newx,newy))
            #print(li)
            return li
        m=len(board)
        n=len(board[0])
        q=deque()
        #new_board=[["X" for i in range(n)] for j in range(m)]
        for i in range(m):
            
                if board[i][0]=='O':
                    q.append((i,0))
                if board[i][n-1]=='O':
                    q.append((i,n-1))
        for j in range(n):
            if board[0][j]=='O':
                q.append((0,j))
            if board[m-1][j]=='O':
                q.append((m-1,j))
        #for each one call a dfs 
        
        
            
            
        
        while len(q)!=0:
            cur=q.popleft()
            
            
            print(f'cur {cur}')
            
            
            board[cur[0]][cur[1]]='#'
            #visited.add(cur)
            for nei in neighbour(cur):
                
                    
                    print(f'nei  {nei}')
                    #visited.add(nei)
                    q.append(nei)
                    #board[nei[0]][nei[1]]='#'
            #print(visited,empty)
        #print(q)
        #multi_bfs(q,board)
        #print(board)
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='#':
                    board[i][j]='O'
        