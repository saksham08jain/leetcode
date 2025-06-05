# Last updated: 5/6/2025, 11:06:42 pm
class DSU:
    def __init__ (self,V):
        self.parents=[i for i in range(V)]
        self.sz=[1]*(V) #size of subtrees
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
        if self.sz[parx]>self.sz[pary]:
            self.parents[pary]=parx
            self.sz[parx]+=self.sz[pary]
        else:
            self.parents[parx]=pary 
            self.sz[pary]+=self.sz[parx]
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def connected(x,y):
            return x[0]==y[0] or x[1]==y[1]
        dsu=DSU(len(stones))
        for i in range(len(stones)):
            for j in range(len(stones)):
                if connected(stones[i],stones[j]):
                    dsu.union(i,j)
        sizes=[0]*len(stones)
        for i in range(len(stones)):
            sizes[dsu.find(i)]+=1
        #print(sizes)
        ans=0
        for x in sizes:
            if x!=0:
                ans+=x-1
        return ans