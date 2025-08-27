# Last updated: 27/08/2025, 16:50:38
class Solution:
    def maxArea(self, height: List[int]) -> int:

        # only move the bottleneck that is whatever is the lesser height 
        # cause moving the greater one would be redundant we would be reducing width without any gain in hehight 
        n=len(height)
        right=n-1 
        left=0
        max_water=0
        while right>left:
            cur_water=(right-left)
            if height[right]>height[left]:
                # right side one is bigger 
                # which means left side is the bottleneck 
                cur_water*=height[left]
                left+=1
            elif height[left]>height[right]:
                cur_water*=height[right]
                right-=1 
            else:
                # both are equal at each point we have the optimal water already then 
                cur_water*=height[left]
                left+=1
                right-=1
            max_water=max(cur_water,max_water)
        return max_water


        