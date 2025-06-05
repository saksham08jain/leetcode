# Last updated: 5/6/2025, 11:07:23 pm
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        len_window=len(s1)
        i=0
        j=len_window-1
        #s2[i..j] is the substring i will be checking for permutation
        count=[0]*26
        for char in s1:
            count[ord(char)-ord('a')]+=1
        #count of initial substring 
        for ptr in range(i,j+1):
            count[ord(s2[ptr])-ord('a')]-=1
        if count==[0]*26:
                return True 
        while(j<len(s2)-1):
            #if count becomes==0
            #return True 
            print(count)

            count[ord(s2[i])-ord('a')]+=1
            i+=1
            j+=1
            count[ord(s2[j])-ord('a')]-=1
            if count==[0]*26:
                return True 
            
        return False