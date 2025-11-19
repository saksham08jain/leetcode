# Last updated: 19/11/2025, 15:47:21
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[] 
        nums.sort()
        n=len(nums)

        def dfs(start,path):
            nonlocal ans 
            ans.append(path[:])
            for i in range(start,n):
                if i!=start and nums[i]==nums[i-1]:
                    continue 
                path.append(nums[i])
                dfs(i+1,path)
                path.pop()
        dfs(0,[])

        return ans 


        