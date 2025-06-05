# Last updated: 5/6/2025, 11:09:56 pm
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited=[[0]*len(board[0]) for i in range(len(board))]
        print(visited)
        self.word=word
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board,j,i,0,visited):
                    return True 
        return False


    def dfs(self,board,x,y,index,visited):
        
        if index==len(self.word):
            return True
        if x<0 or x>=len(board[0]):
            return
        elif y<0 or y>=len(board):
            return
        elif visited[y][x]!=0:
            return 
        elif board[y][x]!=self.word[index]:
            return
        visited[y][x]=1
        print(board[y][x],end =" ")
        
        ans= self.dfs(board,x+1,y,index+1,visited) or self.dfs(board,x,y+1,index+1,visited) or self.dfs(board,x,y-1,index+1,visited) or self.dfs(board,x-1,y,index+1,visited)

        visited[y][x]=0
        return ans
        