# Last updated: 25/09/2025, 08:55:47
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        para_set=set()
        para_set.add('()')
        li=[0,para_set]
        for i in range(2,n+1):
            new_set=set()
            for k in range(1,i):
                for rbs1 in li[i-k]:
                    for rbs2 in li[k]:
                        if k==1:
                            new_set.add('('+rbs1+')')
                        new_set.add(rbs1+rbs2)
            li.append(new_set)
        return sorted(li[n])


















        # #there are only 3 ways to add a pair 
        # # () + ___ 
        # # ___+() 
        # # (____)
        # # hmm but there maybe duplicates how do we deal with it hmm
        # #intersting
        # i=1
        # para_set=set()
        # para_set.add('()')
        # # print(para_set)
        # # i missed the n/2 *2 case 
        # li=[-1,para_set]
        # while i<n:
        #     i+=1

        #     new_set=set() 
        #     # huh even set one doesnt submit hmm 
        #     # did i miss a possibility ?
        #     # which one?
        #     for rbs in para_set:
        #         new_set.add('('+rbs+')')
        #         new_set.add('()'+rbs)
        #         new_set.add(rbs+'()')
        #     if i%2==0:
        #         for rbs in li[i//2]:
        #             new_set.add(rbs*2)
        #     para_set=new_set
        #     li.append(para_set)
        # return sorted(li[n])

        # # li=['()']
        # # num=len(li)
        # # i=1 
        # # while i<n:
        # #     for N in range(num):
        # #         rbs=li[N]
        # #         li.append('('+rbs+')')
        # #         if rbs[-1]+rbs[-2]!='()': #If it ends on a closing bracket adding a closing bracket would lead to duplicates since i can consider that closing bracket as newly added and consider other permutations of n-1 
        # #             li.append(rbs+'()')
        # #         if rbs[0]+rbs[1]!='()': #If it ends on a closing bracket adding a closing bracket would lead to duplicates since i can consider that closing bracket as newly added and consider other permutations of n-1 
        # #             li.append('()'+rbs)

        # #     # What am i saying with this inequa;ities 
        # #     # Even i am not sure 
        # #     # tf i am even saying 
        # #     # mehh why is it so hard to undertsnad what will lead to duplciates mehh 
        # #     #  is hould just use a set and call it a day 
        # #     # F it i will use a set and call it a day 
        # #     li=li[num:]
        # #     i+=1
        # # return li 
       