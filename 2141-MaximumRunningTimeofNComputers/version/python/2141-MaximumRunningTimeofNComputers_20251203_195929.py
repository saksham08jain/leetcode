# Last updated: 03/12/2025, 19:59:29
1class Solution:
2    def maxRunTime(self, n, A):
3        A.sort()
4        su = sum(A)
5        while A[-1] > su // n:
6            n -= 1
7            su -= A.pop()
8        return su // n