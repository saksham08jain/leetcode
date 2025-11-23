# Last updated: 23/11/2025, 20:57:58
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        summ=sum(nums)
        #sum all the numbers 
        minus_one=[float('inf'),float('inf')]#two sentinesl 
        one=[float('inf'),float('inf')] 
        for x in nums:
            if x%3==1:
                one.append(x)
            elif x%3==2:
                minus_one.append(x)
        #assume ans is summ ie we took all numbers 
        #now summ%3 will either be zero -> we are done 
        #if its one we remove minium one of the ones /two muns ones 
        #same thing if summ%3 is -1 , remove  minium of minus ones/two ones 
        one.sort()
        minus_one.sort()
        if summ%3==0:
            return summ
        if summ%3==1:
            summ-=min(minus_one[0]+minus_one[1],one[0])
            return summ 
        summ-=min(one[0]+one[1],minus_one[0])
        return summ