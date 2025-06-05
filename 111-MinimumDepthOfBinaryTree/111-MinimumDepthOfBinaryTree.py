# Last updated: 5/6/2025, 11:09:35 pm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if(root==None):
            return 0
        if(root.right==None and root.left==None):
            
            return 1
        if(root.right):
            path1=1+self.minDepth(root.right)
        else:
            path1=float('inf')
        if(root.left):
            path2=1+self.minDepth(root.left)
        else:
            path2=float('inf')
        return min(path1,path2)