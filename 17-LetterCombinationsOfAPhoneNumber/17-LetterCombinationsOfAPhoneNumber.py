# Last updated: 5/6/2025, 11:10:39 pm
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
                    2: ['a', 'b', 'c'],
                    3: ['d', 'e', 'f'],
                    4: ['g', 'h', 'i'],
                    5: ['j', 'k', 'l'],
                    6: ['m', 'n', 'o'],
                    7: ['p', 'q', 'r', 's'],
                    8: ['t', 'u', 'v'],
                    9: ['w', 'x', 'y', 'z']
                }

        li=[]
        def combUtil(index,string):
            if index==len(digits):
                li.append(string)
                return
            digit=digits[index]
            for char in map[int(digit)]:
                combUtil(index+1,string+char)
        
        if len(digits)==0:
            return []
        combUtil(0,'')
        return li