# Last updated: 14/11/2025, 18:02:40
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:        
        min_candidates=min(candidates)
        def comb(target,start):
            #terminate when ? 
            if target==0:
                return [[]]
            if target<min_candidates:
                return []
            ans_li=[]
            for i in range(start,len(candidates)):
                num=candidates[i]

                li=comb(target-num,i)
                print(num)
                print(li)
                for subli in li:
                    subli.append(num)
                print(li)
                ans_li.extend(li)
            return ans_li
        return comb(target,0)