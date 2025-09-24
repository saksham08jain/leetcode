# Last updated: 24/09/2025, 09:31:29
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left=0
        right=n-1 
        water=0
        leftMax=-1 
        rightMax=-1
        while right>left:
            hRight=height[right]
            hLeft=height[left]
            if hLeft>leftMax:
                # No water can be trapped by any left wall
                leftMax=hLeft
            if hRight>rightMax:
                rightMax=hRight
            # Now water can be trapped 
            # move whatevr pointer is smaller since it is bottlenecking us and also for invariance 
            if rightMax>=leftMax:
                water+=leftMax-hLeft
                left+=1 
            else:
                water+=rightMax-hRight
                right-=1
        return water

        #Actual solutions is two pointer _ water at ith level 
        # the water at any i is the min(rMax,lMax)-height[i]
        #yeah so we do whateevr is blocking the water and use it 
        # idk i was pretty close to the solution iimo 
        # why couldnt i figure it out?? 
        #  btw what about other ways to solve? there must be a stack solution and i do believe a dp solution exits too 
        # damn so many solutions may exists xDD 
        #  you dont need 1000 questions you need 100 questions 10 ways each xDD
# class Solution:
#     def trap(self, height: List[int]) -> int:



#         '''
#         # key insfdcight keep an uncertain variable the water we are not yet sure we would have or not then we can swwep preety easily imo 
#         last_peak_idx=0
#         certain=0 
#         uncertain=0 

#         for i in range(1,n):
#             # two cases current number is less than last height 
#             last_peak_height=last_peak_idx[0]
            
#             if height[i]<last_peak_height:
#                 # we cant yet fill water because what if there is no enclosing on the right?? 
#                 uncertain+=last_peak_height-height[i]
#                 certain+=(height[i]-last_certain_height)*(i-last_peak_idx-1)
#                 uncertain-=height[i]*(i-last_peak_idx-1)
#             else:
#                 # we found a new peak yay 
#                 last_peak_idx=i 
#                 # we are now certain about everything we were uncertain about 
#                 certain+=uncertain 
#                 uncertain=0 
#         return certain 
#         # lets try to dry run this 
#         # let me firts check if the logic is osund 
#         no logic isnt sound although the approach does seem cool will try to make it work for sure , maybe tomoroow if not today 
#          something with last height too 
#          something with overwriting it 
#          id need something like an ordered set though or a tree to seearcrh fast of the last prefix greater than my number 
#         '''
#         # I am unable to find a O(n) solution let me code O(n*h) one though 
#         H=max(height)
#         water=0
#         n=len(height)
#         sorted_heights=sorted(height)
#         sorted_heights.append(0)
#         for j in range(n,0,-1):
#             # iterate from left to rigth
#             h=sorted_heights[j]
#             i=0
#             mul=h-sorted_heights[j-1]
#             while i<n:
#                 left_height=height[i]
#                 # if we find a tower with height>=h we can start counting 
#                 uncertain=0 #until we find the right barrier we cant be sure we will have this much water 
#                 if left_height>=h:
#                     # what will we count?  height less than cur_height
#                     # when will we stop wehn we find right bound that is cur_height>=h 
#                     i+=1 
#                     while i<n and height[i]<h:
#                         # print(f'i {i} height[i] {height[i]} left_height {left_height} uncertain {uncertain} h {h}')
                        
#                         uncertain+=1 
#                         i+=1 
#                     if i<n:
#                         water+=uncertain*mul
#                 else:
#                     i+=1
#         return water

                            
                            
                    
                    
                    
            
        
                



        