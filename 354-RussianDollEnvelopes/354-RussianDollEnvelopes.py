# Last updated: 5/6/2025, 11:07:50 pm

class Solution:
    def lengthOfLIS( self,arr: List[int]) -> int:
        sub=[]
        sub.append(arr[0][1])
        n=len(arr)
        for i in range(1,len(arr)):
            #print(sub)
            if sub[-1]<arr[i][1] :
                sub.append(arr[i][1])
            elif  sub[-1]>arr[i][1]:
                idx=bisect_left(sub,arr[i][1])
                sub[idx]=arr[i][1]
        
        return len(sub)
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        #sort on increasing order on width and decreasing order on height
        for i in envelopes:
            i[1]*=-1

        envelopes.sort()

        for i in envelopes:
            i[1]*=-1
        print(envelopes)
        
        
                

        
        return self.lengthOfLIS(envelopes)

        
