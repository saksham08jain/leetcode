# Last updated: 5/6/2025, 11:10:51 pm
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        
        lent=len(nums)
        zipped=[]
        for i in range(lent):
            zipped.append((nums[i],i))
        zipped.sort()
        ordered,og_indexes=zip(*zipped)
        i=0
        j=lent-1
        #print(ordered)
        while(1):
            #print(i,j)
            tryy=ordered[i]+ordered[j]
            if(tryy>target):
                j-=1
            elif(tryy<target):
                i+=1
            else:
                return og_indexes[i],og_indexes[j]
