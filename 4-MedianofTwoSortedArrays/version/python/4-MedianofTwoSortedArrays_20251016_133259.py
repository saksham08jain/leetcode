# Last updated: 16/10/2025, 13:32:59
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        
        #the key insight is fixing parition in one forces parittion in another array 

        #I will code the general function for better understanding ie find kth element of two sorted arryas without merging in O (log (m+n))
        def get_ele(arr,idx):
                if idx<0:
                    return -float('inf') 
                    #to maintain sorted property 
                elif idx>=len(arr):
                    return float('inf')
                else:
                    return arr[idx]

        def find_kth(nums1,nums2,k):

            
            #Why do the solutions pick up the smaller array ? is it just becaue faster time complexity? 
            #yup looks like it edgecases will always be there  anyway 

            #the key insight is whats kth element 
            # its the element with smallest k elements towards the left 
            #what are smallest k elements? 
            # say first x elements from X and first y (k-x) elemensts from Y 
            #Now such a particion can be found by binary searching only one array since other part is defined by it by k-x 
            # we just need to ensure that we picked smallest k elements for sure for that wwe check the borders of partiion and boom done 
            
            if len(nums1)>len(nums2):
                #Ensure nums1 is the samller array 
                nums1,nums2=nums2,nums1
            m=len(nums1)
            n=len(nums2)

            #m is the samlller length 
            lo=-1 
            hi=m-1 
            #bruh empty array is the issue , what if i make x always the non empty array 
            #no it isnt the solution the issue is get_ele([],0) will return inf 
            #ah yes make low -1 
            #boom done 
            #there are still off by one errors and sheninagags i need to understand but yeah 
            while hi>=lo: 
                mid=(hi+lo)//2
                #mid ie x 
                x=mid
                y=k-x-1 
                #-1 since kth index will have k-1 elements total towards its left 
                print(nums1,nums2)
                print(k,x,y)
                #visualise the parition 
                #copamre with right border 
                if get_ele(nums1,x)>get_ele(nums2,y+1):
                    #not sorted we will need a parition elsewhere 
                    #elif is actually inst needed since these are mutually exculuive conidtions it jut used to chain my else 
                    #go back since going forward maitains this condition due to sorted property 
                    hi=mid-1
                elif get_ele(nums2,y)>get_ele(nums1,x+1):
                    #not sorted we will need a parition elsewhere 
                    #go ahead since going back maintins this condition 
                    lo=mid+1

                else:
                    #got correct parition 
                    #kth element will be minimum of right borders return it 
                    
                    return max(get_ele(nums2,y),get_ele(nums1,x))
        #hmm avg is left median + right median by 2 for odd number it just happens that left median = rigth emdiann 
        m=len(nums1)
        n=len(nums2)
        leftMedian=find_kth(nums1,nums2,(m+n-1)//2)
        rightMedian=find_kth(nums1,nums2,(m+n)//2)
        median= (leftMedian+rightMedian)/2
        return median