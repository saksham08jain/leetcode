# Last updated: 09/11/2025, 12:45:47
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good=0
        def dfs(root,pathMax):
            #path of max till root including root ie 
            if not root:
                return 
            nonlocal good 
            pathMax=max(pathMax,root.val)
            if root.val>=pathMax:
                good+=1
            dfs(root.left,pathMax)
            dfs(root.right,pathMax)
        dfs(root,-float('inf'))
        return good
            
            
        