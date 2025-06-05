# Last updated: 5/6/2025, 11:09:31 pm
class Solution:

    
    def generate(self, numRows: int) -> List[List[int]]:
        li=[[1]]
        for i in range(1,numRows):
            nextrow=[1]
            #summ=0
            prevrow=li[i-1]
                
            for k in range(len(prevrow)-1):

                nextrow.append(prevrow[k]+prevrow[k+1])
            nextrow.append(1)
            li.append(nextrow)
        return li 