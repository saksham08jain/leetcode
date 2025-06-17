# Last updated: 17/6/2025, 5:45:24 pm
class Solution:
    def maxDiff(self, num: int) -> int:
        maxx=0
        x=-1
        num2=num
        idx=8
        while num<10**idx: #0 as a digit wont even be considered ahhh
                idx-=1
        for index in range(idx,-1,-1): #digit by digit 
            
            dgt=num//(10**index)
            
            
            num%=10**index
            if dgt!=9 and x==-1:
                x=dgt 
            
            if dgt==9 or dgt==x:
                maxx+=9*10**index 
            else:
                maxx+=dgt*10**index
           
        x=-1
        
        minn=0
        num=num2
        first=True
        replace=0
        for index in range(idx,-1,-1): 
             
           
            dgt=num//(10**index)
            num%=10**index
            if first:
                if dgt!=1:
                    replace=1
                    x=dgt   
                else:
                    first=False
                    minn+=dgt*10**index
                    isone=True
                    continue
            if dgt!=0 and x==-1:
                if isone and dgt==1:
                    pass
                else:
                    x=dgt 
            # print('dgt',dgt)
            # print('x',x)
            # print('replace',replace)
            if dgt==x:
                minn+=replace*10**index #replace first non zero digit with zeros 
            else:
                minn+=dgt*10**index
            first=False
            
        print("minn",minn)
        print("maxx",maxx)
        return maxx-minn