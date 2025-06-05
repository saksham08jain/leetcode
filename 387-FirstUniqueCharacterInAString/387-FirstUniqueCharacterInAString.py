# Last updated: 5/6/2025, 11:07:43 pm
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count={}
        for i in s:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        for idx,ele in enumerate(s):
            if count[ele]==1:
                return idx
        return -1