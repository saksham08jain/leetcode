# Last updated: 26/08/2025, 13:09:53
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        left=0 
        right=n-1 

        while right>left:
            cur_sum=numbers[left]+numbers[right]
            if cur_sum==target:
                return([left+1,right+1])
            elif cur_sum<target:
                left+=1 
            else:
                right-=1 
    