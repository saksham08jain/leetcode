# Last updated: 5/6/2025, 11:08:51 pm
class Solution:
    def isHappy(self, n: int) -> bool:
                #get number down to 3 digits first by adding square of digits 
        #since if msb of 3digit number!=0 it can be brought down to 2-digit 
        #Now from 2-digit symmetry only 0-49 needs to be evaluated because digits of 05===50 
        #but wait 69-96 59 -95 
        cache={}
        for num in range(100):
            ans=(num%10)**2+(num//10)**2
            #what if ans is 3-digit as can be 
            if (ans!=ans%100):#3-digit
                
                num2=ans%100
                ans=(ans//100)**2
                ans+=(num2%10)**2+(num2//10)**2
            cache[num]=ans
        #print(cache)
        #now apply the operation 1 guarantted <=3 digit number 
        #if 3-digit reduce to 2 (basically one more op)
        #use cache to terminate or not 
        ans=0
        while(n):
            ans+=(n%10)**2
            n//=10
        #print(ans)
        if ans%10==ans:
            #one digit
            if ans==1:
                return True
            
        #print(ans)
        while( ans!=ans%100):
            num2=ans%100
            ans=(ans//100)**2
            ans+=(num2%10)**2+(num2//10)**2
        #print(ans)
        visited=[-1]*100
            
        while(1):
            if ans%10==ans:
                #one digit
                if ans==1:
                    return True
                
            
                
            ans=cache[ans]
            if visited[ans]==1:
                return False
            visited[ans]=1
        
            
