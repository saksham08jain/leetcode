# Last updated: 5/6/2025, 11:06:35 pm
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inDeg, outDeg = defaultdict(int), defaultdict(int)
        for u, v in trust:
            inDeg[v] += 1
            outDeg[u] += 1
        for i in range(1,n+1):
            if inDeg[i] == n-1 and outDeg[i] == 0:
                return i
        return -1
            