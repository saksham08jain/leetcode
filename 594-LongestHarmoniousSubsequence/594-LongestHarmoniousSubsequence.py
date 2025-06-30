# Last updated: 30/6/2025, 1:08:23 pm
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        #brute force O(n2) ,
        #Ordered set O(n log n) 
        #but therere are 2*10^4 numbers only 
        #pref array time O(n), space O(n2)
        #pref array not needed only count needed hence O(n) space O(n) time

        pref={} 
        maxx=0 
        n=len(nums)
        for i in range(n):
            #consider the subseqeunce ends at this number 
            #length of subsequence , either this number is max or min 
            pref[nums[i]]=pref.get(nums[i],0)+1
            
            length=max(pref.get(nums[i]-1,0),pref.get(nums[i]+1,0))
            if length!=0:
                length+=pref[nums[i]]
                maxx=max(length,maxx)
        return maxx