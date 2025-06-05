# Last updated: 5/6/2025, 11:09:50 pm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.li=[]
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        if root.left!=None:
            self.inorderTraversal(root.left)
        self.li.append(root.val)
        if root.right!=None:
            self.inorderTraversal(root.right)
        return self.li