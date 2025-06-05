# Last updated: 5/6/2025, 11:09:29 pm
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curmax=0
        curmin=float('inf')
        lent=len(prices)
        maxxprof=0
        for i in range(lent):

            
            if prices[i]<curmin:
                curmin=prices[i]
            
            curprof=prices[i]-curmin
            if curprof>maxxprof:
                maxxprof=curprof
        return maxxprof