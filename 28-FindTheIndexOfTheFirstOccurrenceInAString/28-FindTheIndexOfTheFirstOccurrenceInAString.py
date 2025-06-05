# Last updated: 5/6/2025, 11:10:28 pm
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hayptr=0
        needptr=0
        index=-1
        count=0
        if len(needle)>len(haystack):
            return -1
        while(hayptr<len(haystack) and needptr<len(needle)):
            
            try:
                while(haystack[hayptr]==needle[needptr]):
                    count+=1
                    if(count==len(needle)):
                        #print(hayptr,count)
                        return hayptr-count+1
                    hayptr+=1
                    needptr+=1
            except:
                return -1
            hayptr=hayptr-count+1
            count=0
            index=-1
            
            #hayptr+=1
            needptr=0
        return index