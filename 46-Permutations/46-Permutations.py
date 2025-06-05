# Last updated: 5/6/2025, 11:10:17 pm
class Solution:
    def permute(self, nums: List[int]):
        res=[]
        return self.permute_util(nums,0)


    def permute_util(self, nums: List[int],start) -> List[List[int]]:
        res=[]
        if len(nums)==start+1:
            return [[nums[start]]]
        for oldperm in self.permute_util(nums,start+1):
            for j in range(start,len(nums)):
                oldperm.insert(j-start,nums[start])
                res.append(oldperm[:])
                #print(res,j,oldperm)
                del oldperm[j-start]
        return res