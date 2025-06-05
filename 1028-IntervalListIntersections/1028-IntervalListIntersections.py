# Last updated: 5/6/2025, 11:06:38 pm
class Solution:
    def intervalIntersection(self, list1: List[List[int]], list2: List[List[int]]) -> List[List[int]]:
        
        #2 pointer 
        #increase pointe of whoever finished ealiest 
        interval=[]
        i=0
        j=0 
        while(i<len(list1) and j<len(list2)):
            start1,end1=list1[i]
            start2,end2=list2[j]
            #intersection case 
            if (start2<=end1 and end2>=start1) or(start1<=end2 and end1>=start2) :
                interval.append([max(start1,start2),min(end1,end2)])
            if end1>end2:
                j+=1
            else:
                i+=1
        return interval