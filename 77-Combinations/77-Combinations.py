# Last updated: 5/6/2025, 11:09:59 pm
class Solution:
    def __init__(self):
        self.li=[]
        
    def combine(self,n,k):
        self.K=k
        return self.combine_util(n,k)
    def combine_util(self, n: int, k: int,chosen=[]):
           

            if k>n or n==-1:
                
                return
            if len(chosen)==self.K:
                self.li.append(chosen.copy())
                return
            self.combine_util(n-1,k,chosen)
            self.combine_util(n-1,k-1,[n]+chosen)
            return self.li
    