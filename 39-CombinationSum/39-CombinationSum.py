# Last updated: 5/6/2025, 11:10:23 pm
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates=candidates
        self.solutions=[]
        self.combSumUtil(target,0)
        return self.solutions
    def combSumUtil(self,target,i,chosen=[]):
        if target<0 or i==len(self.candidates):
            return
        if target==0:
            self.solutions.append(chosen.copy())
            return
        cur=self.candidates[i]
        
        self.combSumUtil(target-cur,i,chosen+[cur])
        #self.combSumUtil(target-cur,i+1,chosen+[cur])
        self.combSumUtil(target,i+1,chosen)  
