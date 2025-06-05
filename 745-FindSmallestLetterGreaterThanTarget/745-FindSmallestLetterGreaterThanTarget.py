# Last updated: 5/6/2025, 11:07:02 pm
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        lo=-1
        hi=len(letters)
        mid=(lo+hi)//2

        while(mid>lo and mid<hi):

            if letters[mid]<=target:
                lo=mid 
            
            else:
                hi=mid
            mid=(lo+hi)//2
        
        #if letters[mid]==target:
        #    mid+=1
        
        return letters[(mid+1)%len(letters)]