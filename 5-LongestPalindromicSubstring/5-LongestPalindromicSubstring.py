# Last updated: 5/6/2025, 11:10:45 pm
class Solution:
    def longestPalindrome(self, arr: str) -> str:
        n=len(arr)
        lps=[['' for i in range(n)] for j in range(n)]
        max_len=0
        max_lps=''
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                
                   
                if j==0 or i==n-1:
                    mid=''
                else:
                    mid=lps[i+1][j-1]
                
                if i==j:
                    lps[i][j]=arr[i]
                    
                elif arr[i]==arr[j]:
                    if mid!='' or j-i==1:
                        lps[i][j]=arr[i]+mid+arr[i]
               
                if len(lps[i][j])>max_len:
                    max_len=len(lps[i][j])
                    max_lps=lps[i][j]


        #print(lps)
        return max_lps