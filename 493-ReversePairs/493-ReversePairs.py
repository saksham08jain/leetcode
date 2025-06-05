# Last updated: 5/6/2025, 11:07:28 pm
#Solution 1: BIT
#Solution 2: Merge Sort Tree 
#Solution 3: binary search?
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
def create_ranking(arr):
    """
    Create rank mapping for an array.
    Returns a rank array where rank[i] gives the rank of arr[i].
    """
    sorted_indices = sorted(range(len(arr)), key=lambda x: arr[x])  # Sort indices by array values
    rank = [0] * len(arr)
    for i, idx in enumerate(sorted_indices, start=1):
        rank[idx] = i
    return [0]+rank
class Solution:
    
    def reversePairs(self, arr):
        n=len(arr)
        for i in range(n):
            arr.append(arr[i]*2)

        rank_arr=create_ranking(arr)
        
        ft=BIT(2*n)
        inv=0 
        for i in range(1,n+1):
            #insert the i th rank 
            inv+=ft.query_lr(rank_arr[i+n],2*n) # numbers above it 
            ft.update(rank_arr[i],1) # add one ,ie instead of doing pref sum , just increase count of that rank
            #print(i,ft.query_lr(rank_arr[i],n))
            
        return(inv)
'''
class Solution:
    #User function Template for python3
    #Function to count inversions in the array.
    # def __init__(self):
    #     self.inv=0
    def mergesort(self,arr, l, r):
        #code here
        inv=0
        if l==r:
            return [arr[r]],0
        mid=(l+r)//2
        
        left,left_inv=self.mergesort(arr,l,mid)
        right,right_inv=self.mergesort(arr,mid+1,r)
        merged,merged_inv=self.merge(arr,left,right)
        two_right=[-1]*len(right)
        for i in range(len(right)):
            two_right[i]=right[i]*2
        two_merged,two_merged_inv=self.merge(arr,left,two_right)
        #print(left,right,merged)
        inv+=left_inv+right_inv+two_merged_inv
        #print(left_inv,right_inv,two_merged_inv)
        return merged,inv
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
            leftele=float('inf')
            rightele=float('inf')
            if l<left_len:
                leftele=left[l]
            if r<right_len:
                rightele=right[r]
            if leftele<=rightele:#equal to for stable sorting 
                new_arr[l+r]=leftele
                l+=1
            else:
                new_arr[l+r]=rightele
                r+=1
            
                inv+=left_len-l
        return new_arr,inv
    def reversePairs(self, arr):
        merged,inv=self.mergesort(arr,0,len(arr)-1)
        return(inv)