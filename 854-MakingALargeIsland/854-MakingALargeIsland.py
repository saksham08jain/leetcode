# Last updated: 5/6/2025, 11:06:53 pm

    
class DSU:
    def __init__ (self,V):
        self.parents=[i for i in range(V)]
        self.sz=[1]*(V+1) #size of subtrees
        self.islands=V 
    def find(self,x):
        #with path compression 
        if x==self.parents[x]:
            return x 
        else:
            self.parents[x]=self.find(self.parents[x])
            return self.parents[x]
    def union(self,x,y):
        parx=self.find(x)
        pary=self.find(y)
        if parx==pary:
            return 
        self.islands-=1
        
        if self.sz[parx]>self.sz[pary]:
            self.parents[pary]=parx
            self.sz[parx]+=self.sz[pary]
        else:
            self.parents[parx]=pary 
            self.sz[pary]+=self.sz[parx]
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def get_nei(x,y):
            d=[(-1,0),(1,0),(0,1),(0,-1)]
            li=[]
            for dx,dy in d:
                nx=x+dx
                ny=y+dy
                #print(nx,ny)
                if (nx>=0 and nx<n) and (ny>=0 and ny<n) and grid[nx][ny]==1:
                    li.append((nx,ny))
            return li
       
        n=len(grid)
        #print('testing',get_nei(0,1))
        dsu=DSU(n*n)
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    for nx,ny in  get_nei(i,j):
                        
                            dsu.union(i*n+j,nx*n+ny)
        #print(dsu.parents)
        #print(dsu.sz)
        ans=max(dsu.sz)
        for i in range(n):
            for j in range(n):
                sz=0
                if not grid[i][j]:
                    #its zero , try making it 1 
                    p=set()
                    
                    for nx,ny in get_nei(i,j):
                        #find parents of its neighbours
                        #print('nei',nx,ny)
                        p.add(dsu.find(nx*n+ny))
                    #print(f'i {i} j {j} p {p}')
                    for par in p:
                        sz+=dsu.sz[par]
                    sz+=1
                    ans=max(ans,sz)

        return ans
        