# Last updated: 07/10/2025, 21:42:27
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window=len(s1)
        if len(s2)<len(s1):
            return False
       
        len_s2=len(s2)
        print(len(s2))
        diff=[0]*26 
        zeros=26 
        # for our answer everything in diff should become zero 
        # number of zeros should become 26 

        for i in range(len(s1)):
            if diff[ord(s1[i])-ord('a')]==0:
                zeros-=1
            diff[ord(s1[i])-ord('a')]+=1
            if diff[ord(s1[i])-ord('a')]==0:
                zeros+=1
           

        
            if diff[ord(s2[i])-ord('a')]==0:
                zeros-=1 
            diff[ord(s2[i])-ord('a')]-=1
            if diff[ord(s2[i])-ord('a')]==0:
                zeros+=1 
            
        if zeros==26:
            return True
        for start in range(len_s2-window):
            
            print(start)
            print(diff)
            end=start+window 
            
            if diff[ord(s2[start])-ord('a')]==0:
                zeros-=1 
            

            diff[ord(s2[start])-ord('a')]+=1 
            if diff[ord(s2[start])-ord('a')]==0:
                zeros+=1 
            if diff[ord(s2[end])-ord('a')]==0:
                zeros-=1 
            diff[ord(s2[end])-ord('a')]-=1 
            if diff[ord(s2[end])-ord('a')]==0:
                zeros+=1 
            
            if zeros==26:
                return True 
        return False
        



