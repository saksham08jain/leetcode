# Last updated: 5/6/2025, 11:06:28 pm
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
        if parx!=pary:
            self.islands-=1
        if self.sz[parx]>self.sz[pary]:
            self.parents[pary]=parx
            self.sz[parx]+=self.sz[pary]
        else:
            self.parents[parx]=pary 
            self.sz[pary]+=self.sz[parx]
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        dsu=DSU(n)
        for u,v in connections:
            dsu.union(u,v)
        islands=dsu.islands # we need ultimate parents 
        #print(dsu.parents)
        ans=islands-1
        
        return ans