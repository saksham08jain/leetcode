# Last updated: 5/6/2025, 11:08:59 pm
class Solution:
    def rotate(self, arr: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(arr)
        k=k%n
        temp=arr[:min(k,n-k)]
        j=-k
        
        for i in range(k):
            arr[i]=arr[j]
            j+=1 
        j=n-1
        i=-1
        print(arr,temp,j,k)
        while(j>=k):
            if(j-k<k):
                arr[j]=temp[i]
                i-=1
            else:
                arr[j]=arr[j-k]
            
            j-=1   
        #print(arr)