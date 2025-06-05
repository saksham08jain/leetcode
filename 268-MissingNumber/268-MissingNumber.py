# Last updated: 5/6/2025, 11:08:13 pm
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        modd=n%4
        mapp={0:n,1:1,2:n+1,3:0}
        xor=mapp[modd]

        for i in nums:
            xor^=i
        return xor