# Last updated: 5/6/2025, 11:06:15 pm
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        a=coins
        added=0 
        add_li=[]
        i=0 
        n=len(coins)
        maxi=0
        while(1):
            if i<n and a[i]<=maxi+1:
                maxi+=a[i]
                i+=1
            else:
               break
                
        #print(add_li)
        return maxi+1