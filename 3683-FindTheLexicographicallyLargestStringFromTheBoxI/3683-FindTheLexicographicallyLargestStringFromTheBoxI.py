# Last updated: 5/6/2025, 11:06:01 pm
class Solution:
    def get_char(self,wrd,idx,offset):
        #returns idx+offset_char_in_sritng
        n=len(wrd)
        if idx+offset>=n:
            return chr(ord('a')-1)
        return wrd[idx+offset]
    def answerString(self, wrd: str, numFriends: int) -> str:
        if numFriends==1:
            return wrd
        maxx=max(wrd)
        n=len(wrd)
        cur_indices=[]
        for i in range(n):
            if wrd[i]==maxx:
                cur_indices.append(i)
        #cur_indices contain strings currently being considered for max , therefore it is always tied 
        for offset in range(1,n):
            new_indices=[]
            maxx=chr(ord('a')-1)
            for idx in cur_indices:
                next_char=self.get_char(wrd,idx,offset)
                if next_char>maxx:
                    maxx=next_char
            for idx in cur_indices:
                next_char=self.get_char(wrd,idx,offset)
                if next_char==maxx:
                    new_indices.append(idx)
            cur_indices=new_indices[:]
        #print(cur_indices)
        #i believe only one item will always be left 
        start=cur_indices[0]
        end=start+n-numFriends+1
        ans=wrd[start:end]
        return ans
        #timecomplexity O(n2) 
        #auto github commit extesnion on leetcode?
        #can i optimise it?
        #hmm i need to think 
        #tomorrow 
        
                    