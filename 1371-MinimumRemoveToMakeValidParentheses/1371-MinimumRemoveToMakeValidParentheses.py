# Last updated: 13/6/2025, 6:53:17 pm
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        running_sum=0 
        removed=0 
        n=len(s)
        news=list(s)
        indexs=[]
        for i in range(n):
            char=s[i]
            if char=='(':
                running_sum+=1
            elif char==')':
                running_sum-=1 
               
            
            if running_sum<0:
                news[i]=''
                running_sum=0 
                removed+=1 
        removed+=running_sum # running_sum >=0 , those extra opening brakctes need to be removed 
        #always remove the last left '(' brackets since they will cause minimal interfercne , no ) is counting on it 
        #i will take O(n) space or i can do a second traversal 
        #i need a second traversal anyway , in that second traversa
        
        for i in range(n-1,-1,-1):
                if running_sum==0:
                        break
                if s[i]=='(':
                    news[i]=''
                    running_sum-=1
                    
        
        return ''.join(news)