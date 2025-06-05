# Last updated: 5/6/2025, 11:06:21 pm
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n=len(s)
        max_len=-1
        def helper(start,seen):
            nonlocal max_len
            cur=''
            if start==n:
                #print(seen)
                max_len=max(max_len,len(seen))
                return
            for i in range(start,n):
                #split at this index 
                cur+=s[i]
                #print(start,cur,seen)
                if cur not in seen:
                    seen.add(cur)
                    #split further 
                    helper(i+1,seen)
                    seen.remove(cur)
        seen=set()
        helper(0,seen)
        return max_len
        '''
        cur=''
        seen=set()
        n=len(s)
        for i in range(n):
            cur+=s[i]
            if cur not in seen:
                #add cur substring to seen 
                print(cur)
                seen.add(cur)
                cur=''
        #print(seen)
        return len(seen)
        '''