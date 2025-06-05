# Last updated: 5/6/2025, 11:10:16 pm
class Solution:
    def permuteUnique(self, nums: List[int]):
        res=[]
        
        return self.permute_util(nums,0)


    def permute_util(self, nums: List[int],start) -> List[List[int]]:
        res=[]
        if len(nums)==start+1:
            return [[nums[start]]]
        oldperms=self.permute_util(nums,start+1)
        for oldperm in oldperms:
            for j in range(start,len(nums)):
                oldperm.insert(j-start,nums[start])
                if oldperm not in res:
                    res.append(oldperm[:])
                #print(res,j,oldperm)
                del oldperm[j-start]
        return res