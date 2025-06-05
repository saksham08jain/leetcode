# Last updated: 5/6/2025, 11:07:00 pm
'''
class Solution:
    def __init__(self):
        #self.permutations=[]
        pass
    def letterCasePermutation(self, s: str,permutations=[]) -> List[str]:
        if len(s)==1:
            if s[0]==s[0].upper() and s[0]==s[0].lower():
                return [s[0]]
            return [s[0].lower(),s[0].upper()]
        newPerms=permutations[:]
        for withoutFirstletter in self.letterCasePermutation(s[1:]):
            print(withoutFirstletter)
            string1=s[0].lower()+withoutFirstletter
            newPerms.append(string1)
            
            string2=s[0].upper()+withoutFirstletter
            if string1!=string2:
                newPerms.append(string2)
        print(newPerms)
        return newPerms
    '''

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(sub="", index=0):
            if index == len(s):
                permutations.append(sub)
                return
            if s[index].isalpha():
                backtrack(sub + s[index].lower(), index + 1)
                backtrack(sub + s[index].upper(), index + 1)
            else:
                backtrack(sub + s[index], index + 1)

        permutations = []
        backtrack()
        return permutations
