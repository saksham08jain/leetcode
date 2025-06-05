# Last updated: 5/6/2025, 11:08:06 pm
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefsum=[]
        self.nums=nums
        lent=len(nums)
        cursum=0
        for i in range(lent):
            cursum+=nums[i]
            self.prefsum.append(cursum)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefsum[right]-self.prefsum[left]+self.nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)