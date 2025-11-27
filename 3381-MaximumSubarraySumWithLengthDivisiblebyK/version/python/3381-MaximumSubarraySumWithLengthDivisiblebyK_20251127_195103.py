# Last updated: 27/11/2025, 19:51:03
1class Solution:
2    def maxSubarraySum(self, nums: List[int], k: int) -> int:
3        maxx=-float('inf')
4        n=len(nums)
5        pref_sum=[0] 
6        #pref[i] excludes [i]
7        cur_sum=0
8        for i in range(n):
9            cur_sum+=nums[i]
10            pref_sum.append(cur_sum)
11
12        for start in range(0,k):
13            cur_maxx=-float('inf')
14            cur_sum=-float('inf')
15            #print(start)
16            for end in range(start+k,n+1,k):
17                to_add=pref_sum[end]-pref_sum[end-k]
18                cur_sum=max(to_add,cur_sum+to_add)
19                maxx=max(cur_sum,maxx)
20        return maxx
21
22