# Last updated: 30/11/2025, 18:46:09
1class Solution:
2    def minSubarray(self, nums: List[int], p: int) -> int:
3        n=len(nums)
4        last_saw={}
5        last_saw[0]=-1
6        x=sum(nums)
7        x%=p
8        #track where i last saw each remainder 
9        cur=0 
10        length=float('inf')
11        for i in range(n):
12            cur+=nums[i]
13            cur_rem=cur%p 
14            last_saw[cur_rem]=i
15
16            reqd_rem=cur_rem-x 
17            reqd_rem%=p
18            
19            length=min(length,i-last_saw.get(reqd_rem,-float('inf')))
20        return -1 if length==n else length
21