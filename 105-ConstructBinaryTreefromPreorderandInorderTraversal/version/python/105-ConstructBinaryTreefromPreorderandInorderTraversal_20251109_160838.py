# Last updated: 09/11/2025, 16:08:38
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def help(preStart,preEnd,inStart,inEnd):
            #but no whats cponintouss in preorder need not be continous inorder , yes but left subtrees preorder and inorder must be same 

            #so consider this is preorder and inorder of a subtree 
            if  preEnd<preStart or inEnd<inStart:
                return None
            root=TreeNode(preorder[preStart])
            # if preEnd-preStart==1:
            #     return root
            #root of subtree 
            #lets try to find left subtree 
            #anything left to the root in inorder belongs to left in inorder and to the right right subtree 
            #subroutine to find roots index in inorder(optimsiatons later , make it work , make it right , make it fast )
            for i in range(inStart,inEnd+1):
                if inorder[i]==root.val:
                    root_idx=i 
                     
            
                
            inLeftStart=inStart 
            inLeftEnd=root_idx-1 
            inRightStart=root_idx+1 
            inRightEnd=inEnd 

            preLeftStart=preStart+1 
            preRightEnd=preEnd
            #wehre does preLEft End 

            #the length of left SubTree is 
            len_left=inLeftEnd-inLeftStart+1
            #this means 
            preLeftEnd=preStart+len_left
            preRightStart=preLeftEnd+1
            root.right=help(preRightStart,preRightEnd,inRightStart,inRightEnd)
            root.left=help(preLeftStart,preLeftEnd,inLeftStart,inLeftEnd)
            return root
        n=len(preorder)
        return help(0,n-1,0,n-1)

