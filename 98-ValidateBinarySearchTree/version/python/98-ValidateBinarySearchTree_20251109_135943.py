# Last updated: 09/11/2025, 13:59:43
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        last=-float('inf')
        def inorder(root):
            nonlocal last
            right=True 
            left=True
            if root.left:
                left=inorder(root.left)
            #process root 
            if root.val<=last:
                
                return False
            last=root.val
            if root.right:
                right=inorder(root.right)
            return right and left 
        return inorder(root)
            
