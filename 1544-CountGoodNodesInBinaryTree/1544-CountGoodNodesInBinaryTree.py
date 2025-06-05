# Last updated: 5/6/2025, 11:06:25 pm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        def solver(root,max):
            nonlocal count
            if(root==None):
                return
            
            if(root.val>=max):
                max=root.val

            solver(root.left,max)
            if root.val>=max:
                count+=1
            #print(root.val,max,count)
            solver(root.right,max)    

        solver(root,float('-inf'))
        return count
        