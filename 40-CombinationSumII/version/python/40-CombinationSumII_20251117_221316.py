# Last updated: 17/11/2025, 22:13:16
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
 

        ans=[] 
        n=len(candidates)
        candidates.sort()
        #i have a hunch sorting should make it better 
        #but it doesnt solve thr probelm 
        #is there no way except keeping a seen hmmm 
        #aha i dont need three twos in first bracnh or any branch 
        #just the first two would suffice 

        def dfs(path,pathsum,start):
            nonlocal ans 
            if pathsum==target:
                ans.append(path[:])
                return 
            if pathsum>target:
                return


            for i in range(start,n):
                if i!=start and candidates[i]==candidates[i-1]:
                    continue 
                    #not doing this will lead to duplicates 
                    #since say. i had 3 twos 
                    #i could explore other twos but thyye get explored anyway below first 2 so yeah 
                    #but its i-1 in python it warps so if i !=0 
                path.append(candidates[i])
                dfs(path,pathsum+candidates[i],i+1)
                path.pop()
            return 
        dfs([],0,0)
        return ans 

        