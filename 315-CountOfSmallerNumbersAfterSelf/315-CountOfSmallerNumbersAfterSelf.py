# Last updated: 5/6/2025, 11:08:00 pm
#Solution 1 :BIT 
'''
class BIT():
    #one indexed
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
 
    def update(self, index, val):
       
        while index <= self.n:
            self.tree[index] += val
            index += index & (-index)
 
    def query(self, r):
        res = 0
        while r > 0:
            res += self.tree[r]
            r -= r & (-r)
        return res
 
    
    def query_lr(self, left, right):
        return self.query(right) - self.query(left - 1)
def create_ranking( arr):
    """
    Create rank mapping for an array.
    Returns a rank array where rank[i] gives the rank of arr[i].
    """
    sorted_indices = sorted(range(len(arr)), key=lambda x: arr[x])  # Sort indices by array values
    rank = [0] * len(arr)
    for i, idx in enumerate(sorted_indices, start=1):
        rank[idx] = i
    return rank
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ranks=create_ranking(nums)
        ft=BIT(n)
        ans=[-1]*(n)
        for i in range(n-1,-1,-1):
            ans[i]=ft.query_lr(0,ranks[i])
            ft.update(ranks[i],1)
        return ans

'''
#Solution 2 : MergeSort 
#link number with its inde x
# inv [numbers[index]]+=r
class Solution:

    def __init__(self):
        self.inv=[]
    def mergesort(self,arr, l, r):
        #code here
        inv=0
        if l==r:
            return [arr[r]]
        mid=(l+r)//2
        
        left=self.mergesort(arr,l,mid)
        right=self.mergesort(arr,mid+1,r)
        merged=self.merge(arr,left,right)
        #print(left,right,merged)
        
        return merged
    def merge(self,arr,left,right):
        left_len=len(left)
        right_len=len(right)
        new_arr=[-1]*(left_len+right_len)
        #new_arr=arr
        l=0 
        r=0 
        inv=0
        while l<left_len or r<right_len:
            #pick smaller element and put in right locarion 
            #so if elements are over we can say theres a infinity 
            leftele=float('inf'),-1
            rightele=float('inf'),-1
            if l<left_len:
                leftele=left[l]
            if r<right_len:
                rightele=right[r]
            if leftele[0]<=rightele[0]:#equal to for stable sorting 
                new_arr[l+r]=leftele
                l+=1
                self.inv[leftele[1]]+=r
            else:
                new_arr[l+r]=rightele
                r+=1
                
        return new_arr
    def inversionCount(self, arr):
        pass
    def countSmaller(self, arr: List[int]) -> List[int]:
        self.inv=[0]*len(arr)
        n=len(arr)
        zipped=list(zip(arr,range(n)))
        #print(zipped)
        merged=self.mergesort(zipped,0,len(arr)-1)
        return(self.inv)