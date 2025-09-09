# Last updated: 09/09/2025, 10:14:06
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Can use a ordered set here 
        # Sas=dly python doesnt have ordered set I can implement one via Fewnick. or segment tree or skip list i will do this later today , after work , i will do all three ,just to learn 
        # Oh there will be a dp solution here too 
        # and one via sorting and keeping two arrays
        # right now lets do the standard monotnic stack approach (yeah normie i know)
        # start from right 
        stack=[]
        n=len(temperatures)
        ans=[0]*n
        # ans for last number will alwyas be zero 
        # since there is no right 
        # we want right and greater 
        # which means left and smaller
        stack.append((temperatures[n-1],n-1))
        for i in range(n-2,-1,-1):
            # we will make teh stack montonic 
            # ie if we find a number which is greater than we will pop the numbers below it , because say 76 is left of 72 anyday 72 is warmer so is 76 but its left so answer is optimal 
            # basically greedy ig 
            # yeah greedy since its stateless
            
            while stack and stack[-1][0]<=temperatures[i]:
                stack.pop()
            if stack:
                T,idx=stack[-1]
               
                ans[i]=idx-i
                
            
                
            stack.append((temperatures[i],i))
        return ans

