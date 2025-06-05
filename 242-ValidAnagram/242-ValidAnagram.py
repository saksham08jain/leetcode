# Last updated: 5/6/2025, 11:08:16 pm
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr=[0]*26
        for i in s:
            arr[(ord(i)-ord('a'))]+=1
        for j in t:
            if arr[ord(j)-ord('a')]==0:
                return False
            else:
                arr[ord(j)-ord('a')]-=1
        if sum(arr)==0:
            return True
