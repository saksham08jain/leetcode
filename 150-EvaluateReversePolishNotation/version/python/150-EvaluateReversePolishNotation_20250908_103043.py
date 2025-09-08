# Last updated: 08/09/2025, 10:30:43
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[] 
        operations='+-*/'
        for char in tokens:
            if char in operations:
                # [13,5,/]=13/5=op1/op2 => op1 is below in stack 
                op2=stack.pop()
                op1=stack.pop() 
                # I wanted to use eval 
                # I will use eval 
               
                if char=='/':
                    sign=1
                    if op1*op2<0:
                        sign=-1
                    stack.append(sign*(abs(op1)//abs(op2)))

                    # heres the issue 6//-132 will give -1 
                    # why python had division like this though ? something to do wiht moduluo consistencyy? 
                    # no it is just floor division 
                    # The division between two integers always truncates toward zero.This part in questions is the point 
                    # this is fine if both are positive 
                    # I need to handle negative case separately 
                    # floor division with sign 



                if char=='+':
                    stack.append(op1+op2)
                if char=='-':
                    stack.append(op1-op2)
                if char=='*':
                    stack.append(op1*op2)

              
            else:
                stack.append(int(char))

        return int(stack.pop())
            

        