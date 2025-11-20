# Last updated: 20/11/2025, 20:15:36
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        max1 = max2 = -1  # Two largest elements in result set
        count = 0
        
        for start, end in intervals:
            # Both points covered
            if start <= max2:
                continue
            
            # One point covered
            if start <= max1:
                count += 1
                max2 = max1
                max1 = end
            
            # No points covered
            else:
                count += 2
                max2 = end - 1
                max1 = end
        
        return count