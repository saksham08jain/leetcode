# Last updated: 5/6/2025, 11:08:32 pm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if(root):
            root.right,root.left=root.left,root.right
        if(root):
            self.invertTree(root.right)
            self.invertTree(root.left)
        return root