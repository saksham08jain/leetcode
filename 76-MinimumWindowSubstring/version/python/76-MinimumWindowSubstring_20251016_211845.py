# Last updated: 16/10/2025, 21:18:45
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict=defaultdict(int)
        for char in t:
            t_dict[char]+=1
        
        rolling_dict=defaultdict(int)
        target_matches=len(t_dict.keys())
        left=-1
        right=0 
        #left is wehre i am at , right is what is about to be added 
        matches=0 
        ansLeft=-1
        ansRight=0
        ans_length=float('inf')
        #number of characters in my rolling dict matching t
        len_s=len(s)
        while right<len_s:
            #try to add right characyer in my rolling_dict 
            #case 1 we encounter a character which is not in t 
          
            if s[right] not in t_dict:
                #this thing cant affect number of matches we found 
                #add this i substring in continue 
                right+=1 
                continue 
            
            else:
                #the right character is in t_dict 
                rolling_dict[s[right]]+=1 
                if rolling_dict[s[right]]==t_dict[s[right]]:
                    #we have a match 
                    matches+=1 
                else:
                    #dont worry if its not equal yet 
                    #do nothing no need to increae match 
                    #but if rolling_dict[s[right]] became greater , yup still dont need to do anything since t is included in window extra thigs are fine 
                    pass 
                if matches==target_matches:
                    #move left and try to minimse the window we have                
                     
                    while left<right:
                        if s[left+1] not in t_dict:
                            #safley move left ahead nothing wrong will happen 
                            left+=1 
                        else:
                            rolling_dict[s[left+1]]-=1
                            if rolling_dict[s[left+1]]<t_dict[s[left+1]]:
                                matches-=1
                                if right-left<=ans_length:
                                    ansRight=right 
                                    ansLeft=left
                                    ans_length=right-left
                                left+=1 

                                break
                            left+=1
                    
                        
                right+=1 


        print(ans_length,ansLeft,ansRight)
        if ans_length==float('inf'):
            return ""
        return s[ansLeft+1:ansRight+1]


