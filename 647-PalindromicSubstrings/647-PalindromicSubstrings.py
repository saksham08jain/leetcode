# Last updated: 5/6/2025, 11:07:14 pm
class Solution:
    def countSubstrings(self, arr: str) -> int:
        n=len(arr)
        ps_count=[[0 for i in range(n)] for j in range(n)]
        count=0
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                
                   
                if j==0 or i==n-1:
                    mid=0
                else:
                    mid=ps_count[i+1][j-1]
                
                if i==j:
                    ps_count[i][j]=1
                    
                elif arr[i]==arr[j]:
                    if mid!=0 or j-i==1:
                        ps_count[i][j]+=1
               
                count+=ps_count[i][j]


        #print(ps_count)
        return count