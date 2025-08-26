# Last updated: 26/08/2025, 12:55:25
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        left=0 
        right=n-1
        # how to remove and strip away everything and turn it into lower case 
        

        while right>left:
            while s[left] in string.punctuation or s[left]==" ":
                left+=1 
                if left>=n:
                    return True
            while s[right] in string.punctuation or s[right]==" ":
                right-=1
                if right<=0:
                    return True
            if s[right].lower()!=s[left].lower():
                return False 
            right-=1 

            left+=1 
            if left>=n or right<=0:
                    return True

        return True