# Last updated: 07/11/2025, 10:17:37
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #path passing through root and path not passing through root two types of paths 
        #actually at each node jsust consider paths turning at that node ie leftDepth+rightDepth
        ans=0
        def dfs(root):
            nonlocal ans
            #returns leftdepth,rigthdepth
            if not root:
                return -1,-1
            #not passing through root 

            #daimeter is simply the max of right and left subtree 

            rightDepth=1+max(dfs(root.right)) #max of a tuple 
            leftDepth=1+max(dfs(root.left))
            ans=max(rightDepth+leftDepth,ans)


            return leftDepth,rightDepth
        dfs(root)
        return ans
