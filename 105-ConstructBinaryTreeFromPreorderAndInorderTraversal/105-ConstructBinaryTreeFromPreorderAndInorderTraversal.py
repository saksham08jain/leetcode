# Last updated: 5/6/2025, 11:09:42 pm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self,preorder, inorder):

        in_map = {val: idx for idx, val in enumerate(inorder)}
        def buildTreeHelper(preorder, preStart, preEnd, inorder, inStart, inEnd, in_map):
            if preStart > preEnd or inStart > inEnd:
                return None

            root_val = preorder[preStart]
            root = TreeNode(root_val)
            in_root = in_map[root_val]
            nums_left = in_root - inStart

            root.left = buildTreeHelper(preorder, preStart + 1, preStart + nums_left, inorder, inStart, in_root - 1, in_map)
            root.right = buildTreeHelper(preorder, preStart + nums_left + 1, preEnd, inorder, in_root + 1, inEnd, in_map)

            return root

        return buildTreeHelper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, in_map)


