# Last updated: 29/09/2025, 18:08:44
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.map=defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp,value))
        # append the tuple 
        

    def get(self, key: str, timestamp: int) -> str:
        tv_arr=self.map[key]
        # binary search the tv_arr based on timestamp and return value 
        lo=0 
        hi=len(tv_arr)-1
        ans=""
        while hi>=lo:
            mid=(hi+lo)//2
            prev_time,val=tv_arr[mid]
            if prev_time>timestamp:
                hi=mid-1
            else:
                ans=val
                lo=mid+1
        return ans
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)