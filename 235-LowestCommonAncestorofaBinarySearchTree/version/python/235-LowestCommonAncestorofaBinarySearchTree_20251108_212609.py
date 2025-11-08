# Last updated: 08/11/2025, 21:26:09
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur=root 
        while cur and (cur.val-p.val)*(cur.val-q.val)>0:
            if (cur.val-p.val)<0:
                cur=cur.right
            else:
                cur=cur.left
        return cur 
        