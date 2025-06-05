# Last updated: 5/6/2025, 11:09:17 pm
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length=len(s)
        memo=[-1]*(length+1)
        memo[length]=1
        def breakUtil(index):
            sub=''
            if memo[index]!=-1:
                return memo[index]==1
            ans=False
            for i in range(index,length):
                sub+=s[i]
                if sub in wordDict:
                    ans=True and breakUtil(i+1) 
                    if ans:
                        memo[index]=1
                        return ans
            memo[index]=0
            return ans
        return breakUtil(0)