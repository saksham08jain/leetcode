# Last updated: 5/6/2025, 11:06:07 pm
class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        maxi=0
        coins.sort()
        a=coins
        added=0 
        add_li=[]
        i=0 
        n=len(coins)
        while(maxi<target):
            if i<n and a[i]<=maxi+1:
                maxi+=a[i]
                i+=1
            else:
                added+=1
                add_li.append(maxi+1)
                maxi+=(maxi+1)
                
        #print(add_li)
        return added
