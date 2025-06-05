# Last updated: 5/6/2025, 11:08:24 pm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#study binary lifting also 
class Solution:
    #this function is whats wrong 
    #path is still not correct 
    #wondner whats wrong and how can i do better 
    def r2node(self,root,p,curpath=[]):
        path=[]
        def helper(root,p,curpath=[]):
            #returns the path from root to node p 
            nonlocal path
            if root==p:
                curpath.append(p)
                path=curpath
                return
            if root==None:
                return
            if root.right:
                helper(root.right,p,curpath+[root])
            if root.left:
                helper(root.left,p,curpath+[root])
        helper(root,p,curpath=[])
        return path
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #approach 1 store parents in a hasmap go up till common
        #apporach 2 same but just store parents in the path 
        
        path2p=self.r2node(root,p)
        
        path2q=self.r2node(root,q)
        print(f'length of path2p {len(path2p)}')
        
        print('path2p')
        for i in path2p:
            print(i.val,end=' ')
        print()
        print(f'length of path2q {len(path2q)}')
        print('path2q')
        for i in path2q:
            print(i.val,end=' ')
        i=0 
        
        while(i<len(path2p) and i<len(path2q) and path2p[i]==path2q[i]):
            
            i+=1
        
        return(path2p[i-1])
