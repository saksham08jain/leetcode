# Last updated: 09/11/2025, 14:08:40
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=-1 
       
        def inorder(root):
            nonlocal k,ans
            if root.left:
                inorder(root.left)
            #root 
            k-=1 
            if k==0:
                ans= root.val 
                return 
            if root.right:
                inorder(root.right)
            
        inorder(root)
        return ans