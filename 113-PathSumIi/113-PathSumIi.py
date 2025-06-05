# Last updated: 5/6/2025, 11:09:32 pm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root==None:
            return []
        def r2node(root,targetSum,curpath=[]):
            path=[]
            def helper(root,target,curpath=[]):
                #returns the path from root to node p 
                nonlocal path
                #print(curpath,target)
                if root.left==None and root.right==None and root.val==target:
                    curpath.append(root.val)
                    path.append(curpath)
                    return
                if root==None:
                    return
                if root.right:
                    
                    helper(root.right,target-root.val,curpath+[root.val])
                if root.left:
                    helper(root.left,target-root.val,curpath+[root.val])
            helper(root,targetSum)
            return path
        return r2node(root,targetSum)