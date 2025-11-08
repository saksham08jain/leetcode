# Last updated: 08/11/2025, 19:34:26
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

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (root==None):
            return subRoot==None
        if(root.val==subRoot.val):
            #check if this is a subtree 
            same=self.isSameTree(root,subRoot)
            if(same):
                return True 
        #so they werent same 
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        