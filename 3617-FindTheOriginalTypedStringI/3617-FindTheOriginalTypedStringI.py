# Last updated: 24/08/2025, 18:03:35
class Solution:
    def possibleStringCount(self, word: str) -> int:
        #I am not thinking due to speed , i didnt eve stop to undertsand the problem :/
        
        ans=1
        n=len(word)
        prev=word[0]
        
        for i in range(1,n):
            if word[i]==prev:
                ans+=1
            prev=word[i]
        return ans
        
        