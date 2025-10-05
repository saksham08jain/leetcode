# Last updated: 05/10/2025, 22:47:07
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev_min=float('inf')
        max_prof=0
        n=len(prices)
        for i in range(n):
            # treat current day as when i sell and i but when at prev_min 
            prof=prices[i]-prev_min
            prev_min=min(prev_min,prices[i])
            max_prof=max(max_prof,prof)
        return max_prof
        