# Last updated: 5/6/2025, 11:06:26 pm
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist=[[0 if i==j else float('inf') for i in range(n)] for j in range(n)]
        #print(dist )
        for u,v,w in edges:
            dist[u][v]=w
            dist[v][u]=w
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if dist[j][i]+dist[i][k]<dist[j][k]:
                        dist[j][k]=dist[j][i]+dist[i][k]
        #print(dist)
        minncount=float('inf')
        for i in range(n-1,-1,-1):
            count=0
            for j in range(n):
                if dist[i][j]<=distanceThreshold:
                    count+=1
            #print(i,count)
            if count<minncount:
                minncount=count
                maxi=i
        return maxi
