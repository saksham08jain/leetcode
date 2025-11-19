# Last updated: 19/11/2025, 10:43:33
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        available=set(nums)
        def dfs( path: list):
            nonlocal available
            if not available:
                result.append(path)
                return
            
            for num in list(available):
                available.remove(num)
                dfs(path + [num])
                available.add(num)
        
        dfs([])
        return result