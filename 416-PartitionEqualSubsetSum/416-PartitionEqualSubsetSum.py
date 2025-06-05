# Last updated: 5/6/2025, 11:07:35 pm
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1:
            return False
        target=sum(nums)//2
        seen=set()
        seen.add(0)
        for i in nums:
            for j in list(seen):
                seen.add(i+j)
        print(seen)
        return target in seen
            