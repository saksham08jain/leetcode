# Last updated: 5/6/2025, 11:08:11 pm
class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(arr)
        i=0#current 
        j=-1#j is the index of start of zero
        for i in range(n):#gotta see each element 
            
            if(arr[i]==0 and j==-1):
                j=i # first zero 

            elif arr[i]==0:
                pass
            else:
                #print(j,i)
                if(j!=-1):
                    arr[j],arr[i]=arr[i],arr[j]
                    j+=1
            #print(f'i={i},j={j}')
            #print(arr)
        return arr