# Last updated: 5/6/2025, 11:09:49 pm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #arr=[]
        prev=-float('inf')
        ans=True
        def inorder(root):
            nonlocal prev,ans
            #print(root,prev)
            if root.left:
                inorder(root.left)
                
            #process root 
            if root.val<=prev:
                ans=False
                return 
            prev=root.val
            if root.right:
                inorder(root.right)
                
             
        inorder(root)
        return ans