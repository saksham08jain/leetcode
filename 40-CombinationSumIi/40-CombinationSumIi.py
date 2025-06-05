# Last updated: 5/6/2025, 11:10:22 pm
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates=sorted(candidates)#need to sort , figure out why , without sorting not getting [1,2,5]
        self.solutions=[]
        visited=[False]*len(self.candidates)
        self.combSumUtil(target,0,[],visited)
        
        return self.solutions
    def combSumUtil(self,target,i,chosen=[],visited=[]):
        if target<0 :
            return
        if target==0:
            self.solutions.append(chosen.copy())
            return
        if i==len(self.candidates):
            return
        cur=self.candidates[i]
        
        if not visited[i]:
            visited[i]=True
            if  i>0 and cur==self.candidates[i-1]:
                if visited[i-1]:
                    self.combSumUtil(target-cur,i+1,chosen+[cur],visited)
            else:
                self.combSumUtil(target-cur,i+1,chosen+[cur],visited)
            visited[i]=False
        #self.combSumUtil(target-cur,i+1,chosen+[cur])
        self.combSumUtil(target,i+1,chosen,visited)  
