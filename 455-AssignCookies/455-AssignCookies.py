# Last updated: 5/6/2025, 11:07:30 pm
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans=0
        gptr=0
        ans=0

        for i in range(len(s)):
            if gptr==len(g):
                break
            if s[i]>=g[gptr]:
                ans+=1
                gptr+=1
                #i+=1
            #else:
            #    gptr+=1
        return(ans)