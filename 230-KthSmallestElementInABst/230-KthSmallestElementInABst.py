# Last updated: 5/6/2025, 11:08:30 pm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count=0
        ans=0
        def inorder(root):
            nonlocal count,ans
            if(not root):
                return 

            inorder(root.left)
            count+=1
            if(count==k):  
                ans=(root.val)
            

            inorder(root.right)
                
            
        inorder(root)
        return ans