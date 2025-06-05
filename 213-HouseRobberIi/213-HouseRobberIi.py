# Last updated: 5/6/2025, 11:08:38 pm
class Solution:
    def rob(self,nums):
        if len(nums)==1:
            return nums[0]
        return max(self.rob1(nums[1:]),self.rob1(nums[:len(nums)-1]))
    def rob1(self, nums: List[int]) -> int:
        self.cache=[-1]*len(nums)
        ans1=self.rob_help(nums,0)
        ans2=self.rob_help(nums,1)

        print(self.cache)
        return max(ans1,ans2)
    def rob_help(self, nums: List[int],start) -> int:
        if len(nums)-start<=0:
            return 0
        if self.cache[start]!=-1:
            return self.cache[start]
        
            
            
        path1=nums[0+start]+self.rob_help(nums,start+2)
        
           
        try:
           
           
            path2=nums[1+start]+self.rob_help(nums,start+3)
        except:
            
                
                path2=0
        self.cache[start]=max(path1,path2)
        return self.cache[start]
        