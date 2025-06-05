# Last updated: 5/6/2025, 11:07:05 pm
from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def neighbour(cur):
            li = []
            deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for d in deltas:
                nei = (cur[0] + d[0], cur[1] + d[1])
                if 0 <= nei[0] < m and 0 <= nei[1] < n and image[nei[0]][nei[1]] == original_color:
                    li.append(nei)
            return li

        original_color = image[sr][sc]
        if original_color == color:
            return image
        
        m, n = len(image), len(image[0])
        q = deque([(sr, sc)])
        image[sr][sc] = color  # Mark as visited by changing color
        
        while q:
            cur = q.popleft()
            for nei in neighbour(cur):
                q.append(nei)
                image[nei[0]][nei[1]] = color  # Mark as visited when added to queue

        return image
