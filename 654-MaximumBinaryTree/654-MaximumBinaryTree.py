# Last updated: 5/6/2025, 11:07:12 pm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(low,hi):
            maxx=-1
            max_idx=-1
            for i in range(low,hi+1):
                #i am including hi 
                if nums[i]>maxx:
                    maxx=nums[i]
                    max_idx=i
            if maxx==-1:
                return None 
            root=TreeNode(maxx)
            root.left=build(low,max_idx-1)
            root.right=build(max_idx+1,hi)
            return root 
        return build(0,len(nums)-1)