# Last updated: 5/6/2025, 11:06:48 pm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        #recurse , but i need to know the parent 
        #store parents in a hasmap 
        parents={}
        def inorder(root):
            if root.left:
                inorder(root.left)
                #process root 
                parents[root.left.val]=root
            if root.right:
                inorder(root.right)
                parents[root.right.val]=root
        inorder(root)
        parents[root.val]=None
        arr=[]
        visited={}
        def helper(target,k):
            if target in visited:
                return
            visited[target]=True
            if target==None:
                return
            if k==0:
                arr.append(target.val)
                return 
            #if target.right and not visited[target.right]:
            helper(target.right,k-1)
            #if target.left and not visited[target.left]:
            helper(target.left,k-1)
            #if target!=root:
            helper(parents[target.val],k-1)
        helper(target,k)
        return arr