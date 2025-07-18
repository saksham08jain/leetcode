# Last updated: 5/6/2025, 11:09:43 pm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root==None:
            return 0

        return max(1+self.maxDepth(root.right),1+self.maxDepth(root.left))