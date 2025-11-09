# Last updated: 09/11/2025, 18:04:16
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
      
        def help(root):
           
            #returns two things 
            #first is path sum if passing through this node 
            #second is path sum if not passing thorugh this node 

            if not root:
                return -float('inf'),-float('inf')
           
            leftPass,leftNotPass=help(root.left)
            rightPass,rightNotPass=help(root.right)

            #the maximum sum not passing through my current node can be 
            notPass=max(leftPass,rightPass,leftNotPass,rightNotPass,leftPass + rightPass + root.val)

            #maximum sum if passing through current node 
            pas=max(leftPass+root.val,rightPass+root.val,root.val)
            return pas,notPass 
        ans=max(help(root))
        
       
        return ans
        