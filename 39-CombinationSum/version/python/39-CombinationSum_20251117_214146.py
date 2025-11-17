# Last updated: 17/11/2025, 21:41:46
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:        
        ans=[]
        #it will store list of combinations 
        #everything is a graphhh !! 
        n=len(candidates)
        def dfs(path,pathsum,start):
            #store the path and pathsum but wait if i have path do i need pathsum , ah weel lets keep it would avoid summing the path everytime 
            nonlocal ans
            if pathsum==target:
                ans.append(path[:])
                return
            if pathsum>target:
                return 
            for i in range(start,n):
                #ahhaa 
                #duplicates [2,2,3] and [3,2,2] for example hmmm 
                #so lets do one thing 2 will have children 2,3,6,7 3 will have 6,7 , 6 will have 7 and 7 will have no children boom done 
                num=candidates[i]
                path.append(num)
                dfs(path,pathsum+num,i)
                path.pop() 
            return 
        dfs([],0,0)
        return ans 
