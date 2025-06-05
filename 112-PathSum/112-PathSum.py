# Last updated: 5/6/2025, 11:09:34 pm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if(root==None):
            return False
        if(root.left==None and root.right==None):
            return root.val==targetSum
        if(root.left):
            path1=self.hasPathSum(root.left,targetSum-root.val)
        else:
            path1=False
        if(root.right):
            path2=self.hasPathSum(root.right,targetSum-root.val)
        else:
            path2=False
        return path1 or path2