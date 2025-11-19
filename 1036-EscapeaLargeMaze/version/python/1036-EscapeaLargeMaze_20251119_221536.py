# Last updated: 19/11/2025, 22:15:36
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        #i think the only way to make escape impossible is either s or t are completely blocker 
        #or both 
        #one exception is if they are blocked in the same block 
        #for simplicity i am not worrying about exact details 
        #but for sure if a dfs from s  and t can reach a cell which isnt blocked and >blocked.length then they can be reached 
        #or check if they are in the same block hmmm 
        #?? 
        #by this depth ie depth of blockade i am sure that i can reach some cell outside so 
        #so we'd do two dfs with max depth blockade.length from soruce and target 
        #if we can cross this depth we are free 
        #worst case tc = block.length squared 
        #aha not depth i need to use manhattan distancee hmm ?
        #yup done just i need to code it up 

        #checked the comments and someone is saying this soolution doenst work on traingle diagnol 200 
        #other was saying about circle or something and 200*(200-1)
        #coordinate compression hmm ? 
   
        blocked = set(map(tuple, blocked))

        def dfs(x, y, target, seen):
            if not (0 <= x < 10**6 and 0 <= y < 10**6) or (x, y) in blocked or (x, y) in seen: return False
            seen.add((x, y))
            if len(seen) > 20000 or [x, y] == target: return True
            return dfs(x + 1, y, target, seen) or \
                dfs(x - 1, y, target, seen) or \
                dfs(x, y + 1, target, seen) or \
                dfs(x, y - 1, target, seen)
        return dfs(source[0], source[1], target, set()) and dfs(target[0], target[1], source, set())