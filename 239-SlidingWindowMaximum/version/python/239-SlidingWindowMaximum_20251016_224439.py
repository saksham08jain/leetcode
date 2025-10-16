# Last updated: 16/10/2025, 22:44:39
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        #huh why is this hard 
        #just use a sorted  container 
        #duplicates? 
        #easily handled , can be done in n log k hence 
        sl=SortedList() 
        maxx=[] 
        n=len(nums)
        for i in range(k):
            sl.add(nums[i])
        maxx.append(sl[-1])
        for i in range(n-k):
            sl.remove(nums[i])
            sl.add(nums[i+k])
            maxx.append(sl[-1])
        return maxx


