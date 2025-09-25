# Last updated: 25/09/2025, 19:22:25

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
       
        stack=[] #(height,index)
        
    #    the stack waits for things to close 
    # whenever i find a smaller height i close all the heights gretaer than it and the smaller height taakes the index of the last height i removed 
        n=len(heights)
        maxArea=0
        heights.append(0)
        for i in range(n+1):
            lastIdx=i
            while stack and stack[-1][0]>heights[i]:
                # we found a smaller height we can close the past
                lastH,lastIdx=stack.pop() 
                area=lastH*(i-lastIdx)
                maxArea=max(maxArea,area)
            stack.append((heights[i],lastIdx))

        return maxArea
            


        