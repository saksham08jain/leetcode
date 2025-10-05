# Last updated: 05/10/2025, 23:57:01
import string 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # pick a letter which you will try to make maximum 
        # keep sldiing window with atmax k non A characters 
        # when you are our slide left pointer to gain more A characters then continue sliding right pointer 
        # invariant sliding window alsways have same letter 
        ans=1
        
        n=len(s)
        for char in string.ascii_uppercase:
            avl=k 
            left=0 
            right=0 
            while right<n:
                
                
                # now i have atleast one avl 
                #  i can move right once space 
                if s[right]!=char:
                    while avl==0:
                    
                        if s[left]!=char:
                            avl+=1 
                        
                        left+=1 
                    avl-=1 
                right+=1 
                ans=max(right-left,ans)
        return ans
            
                

            
            

                

