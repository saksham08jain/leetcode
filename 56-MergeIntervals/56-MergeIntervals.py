# Last updated: 5/6/2025, 11:10:10 pm
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i=1
        j=0
        final=[intervals[0]]
        while(i<len(intervals)):
            
            if  intervals[i][0]<=final[j][1]:
                #merge then 
                
                final[j]=(min(final[j][0],intervals[i][0]),max(final[j][1],intervals[i][1]))
                i+=1
            else:
                final.append([intervals[i][0],intervals[i][1]])
                i+=1
                j+=1
        
        return final