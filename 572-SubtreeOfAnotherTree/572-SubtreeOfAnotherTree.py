# Last updated: 5/6/2025, 11:07:21 pm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def iseq(self,tree1,tree2):
        if(tree1==None):
            return tree2==None
        if(tree2==None):
            return tree1==None
        return self.iseq(tree1.right,tree2.right) and self.iseq(tree1.left,tree2.left) and tree1.val==tree2.val
        

    def isSubtree(self, root, subRoot) -> bool:
        try:
            return self.iseq(root,subRoot) or self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)
        except AttributeError:
            return False