# Last updated: 5/6/2025, 11:08:25 pm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca=root
        while(p.val-lca.val)*(q.val-lca.val)>0:
            
            if p.val-lca.val<0 and q.val-lca.val<0:
                lca=lca.left
            elif p.val-lca.val>0 and q.val-lca.val>0:
                lca=lca.right 
        return lca