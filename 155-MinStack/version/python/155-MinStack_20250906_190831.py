# Last updated: 06/09/2025, 19:08:31
class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[float('inf')]
        

    def push(self, val: int) -> None:
        
        cur_min=self.getMin()
        if val<=cur_min:
            self.min_stack.append(val)

        # repsect the contraint 
        self.stack.append(val)
        

    def pop(self) -> None:
        val=self.stack.pop() 
        if val==self.getMin(): #The value being popped cant be less than cur_min since we pushed it on min stack 
        # this is our invariant that min stack is monotonic
            self.min_stack.pop()
        return val
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()