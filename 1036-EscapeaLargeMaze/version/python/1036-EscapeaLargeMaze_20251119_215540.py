# Last updated: 19/11/2025, 21:55:40
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
        blocked = {tuple(p) for p in blocked}

        def bfs(source, target):
            bfs, seen = [source], {tuple(source)}
            for x0, y0 in bfs:
                for i, j in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    x, y = x0 + i, y0 + j
                    if 0 <= x < 10**6 and 0 <= y < 10**6 and (x, y) not in seen and (x, y) not in blocked:
                        if [x, y] == target: return True
                        bfs.append([x, y])
                        seen.add((x, y))
                if len(bfs) == 20000: return True
            return False
        return bfs(source, target) and bfs(target, source)
