# Last updated: 5/6/2025, 11:09:23 pm
class Solution:
    def partition(self, s: str) -> List[List[str]]:
       
        li=[]
        def ispalin(s):
            return s==s[::-1]
        def partitionUtil(index,split=[]):
            sub=''
            while(index<len(s)):
                sub+=s[index]
                index+=1 
                if ispalin(sub):
                    
                    split.append(sub)
                    if index==len(s):
                        print(split)
                        li.append(split.copy())
                        
                    partitionUtil(index,split)
                    split.pop() #need to understand prorperly reference to ther list 
                    #split[:-1] wont work casue new reference
                    
            

            
        partitionUtil(0,[])
        return li