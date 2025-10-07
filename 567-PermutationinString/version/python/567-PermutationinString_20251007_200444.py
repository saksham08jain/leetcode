# Last updated: 07/10/2025, 20:04:44
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window=len(s1)
        if len(s2)<len(s1):
            return False
       
        len_s2=len(s2)
        print(len(s2))
        count_s1=[0]*26 
        count_window=[0]*26
        for char in s1:
            count_s1[ord(char)-ord('a')]+=1
        
        # initial count of window 
        for i in range(window):
            count_window[ord(s2[i])-ord('a')]+=1

        for start in range(len_s2-window):
            # check if current window is a match 
            print(start)
            print(count_window)
            
            if count_s1==count_window:
                return True 
            

            end=start+window #end is exluded 
            # we want that s2 has a permuatiaion of s1 
            # this means we want that all characters in s1 appear consecutively here and same frequency 
            # we can compare count of 26 lowercase characters 
            # the count for window can be updated without a for 
            # update count of our roling window ie 
            # subtract start add end 
            count_window[ord(s2[start])-ord('a')]-=1 
            
            count_window[ord(s2[end])-ord('a')]+=1 
        

   
        if count_s1!=count_window:
            return False 
          
        return True


