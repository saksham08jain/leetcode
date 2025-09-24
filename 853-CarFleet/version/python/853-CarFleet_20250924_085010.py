# Last updated: 24/09/2025, 08:50:10
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # I have one approach but i should continue looking for other approached too 
        pos_time=[]
        n=len(position)
        for i in range(n):
            pos=position[i]
            time=(target-pos)/(speed[i])
            tup=(pos,time)
            pos_time.append(tup)
        pos_time.sort(reverse=True)

        fleets=0
        last_time=-float('inf')
        for pos,time in pos_time:
            # instead of explicitly using time since it is division i can avoid it enitrely too 
            if time>last_time:
                fleets+=1
                last_time=time 
            else:
                continue 
        return fleets
