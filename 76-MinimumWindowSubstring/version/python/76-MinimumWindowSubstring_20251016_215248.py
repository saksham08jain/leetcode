# Last updated: 16/10/2025, 21:52:48
class Solution:
    def minWindow(self,s: str, t: str) -> str:
        map_chars = {}
        for c in t:
            map_chars[c] = map_chars.get(c, 0) + 1
        
        counter = len(t)
        begin = 0
        end = 0
        d = float('inf')
        head = 0
        
        while end < len(s):
            if s[end] in map_chars:
                if map_chars[s[end]] > 0:
                    counter -= 1
                map_chars[s[end]] -= 1
            end += 1
            
            while counter == 0:  # valid window
                if end - begin < d:
                    d = end - begin
                    head = begin
                
                if s[begin] in map_chars:
                    map_chars[s[begin]] += 1
                    if map_chars[s[begin]] > 0:
                        counter += 1
                begin += 1
        
        return "" if d == float('inf') else s[head:head + d]