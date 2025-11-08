# Last updated: 08/11/2025, 19:14:19
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def help(root):
            #returns height and -1 if imbalanced 
            if(not root):
                return 0
            rH=help(root.right)
            lH=help(root.left)
            if abs(rH-lH)>1 or rH==-1 or lH==-1 :
                return -1 
            return max(rH,lH)+1
        return help(root)!=-1

            