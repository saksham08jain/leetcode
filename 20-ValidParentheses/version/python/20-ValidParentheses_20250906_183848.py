# Last updated: 06/09/2025, 18:38:48
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
            if char in '({[':
                # if its an opening bracket 
                stack.append(char)
            else:
                #it is a closing bracket , but all i can close is the last open 
                if len(stack)==0:
                    return False
                complement=stack.pop() 
                pair=complement+char
                # wrong pair
                if pair=='()' or pair=='{}' or pair=='[]':
                    continue 
                return False
        if len(stack)!=0:
            return False 
        return True
