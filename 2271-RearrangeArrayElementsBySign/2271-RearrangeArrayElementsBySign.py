# Last updated: 5/6/2025, 11:06:09 pm
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        n=len(nums)
        for num in nums:
            if num>0:
                pos.append(num)
            else:
                neg.append(num)
        new_arr=[]
        for i in range(n):
            if i&1:
                new_arr.append(neg[i//2])
            else:
                new_arr.append(pos[i//2])
        return new_arr
        