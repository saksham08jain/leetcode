# Last updated: 5/6/2025, 11:08:35 pm
class Solution:
    def combinationSum3(self,k,target) -> List[List[int]]:
        self.candidates=[1,2,3,4,5,6,7,8,9]
        self.solutions=[]
        self.K=k
        visited=[False]*len(self.candidates)
        self.combSumUtil(target,0,[],visited,k)
        
        return self.solutions
    def combSumUtil(self,target,i,chosen=[],visited=[],k=0):

        if target<0 :
            return
        if k>self.K:
            return
        if target==0 and len(chosen)==self.K:
            self.solutions.append(chosen.copy())
            return
        if i==len(self.candidates):
            return
        cur=self.candidates[i]
        
        if not visited[i]:
            visited[i]=True
            if  i>0 and cur==self.candidates[i-1]:
                if visited[i-1]:
                    self.combSumUtil(target-cur,i+1,chosen+[cur],visited,k-1)
            else:
                self.combSumUtil(target-cur,i+1,chosen+[cur],visited,k-1)
            visited[i]=False
        #self.combSumUtil(target-cur,i+1,chosen+[cur])
        self.combSumUtil(target,i+1,chosen,visited,k)  