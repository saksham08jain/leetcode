# Last updated: 07/11/2025, 09:33:39
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        newr=self.invertTree(root.left)
    
        newl=self.invertTree(root.right)
        root.right=newr
        root.left=newl
        return root 

        