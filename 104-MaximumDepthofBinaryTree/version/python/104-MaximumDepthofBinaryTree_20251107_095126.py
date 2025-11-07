# Last updated: 07/11/2025, 09:51:26
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #returns maxDepth of root 
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
