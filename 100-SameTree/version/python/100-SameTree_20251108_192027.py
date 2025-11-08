# Last updated: 08/11/2025, 19:20:27
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #current node must have same value 
        if p==None or q==None:
            return p==q
        if p.val!=q.val:
            return False 
        #right and left subtrees must be same 
        right=self.isSameTree(p.left,q.left)
        left=self.isSameTree(p.right,q.right)
        return right and left

        