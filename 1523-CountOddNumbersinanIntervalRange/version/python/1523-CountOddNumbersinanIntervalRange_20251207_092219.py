# Last updated: 07/12/2025, 09:22:19
1class Solution:
2    def countOdds(self, low: int, high: int) -> int:
3        nums=high-low+1
4        nums//=2 
5        if(low%2!=0 and high%2!=0):
6            nums+=1
7        return nums