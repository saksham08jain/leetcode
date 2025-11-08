# Last updated: 08/11/2025, 21:41:23
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()

        traversal=[]
        if root:
            q.appendleft(root)

        while len(q)!=0:
            nq=deque()
            #keep a levle in the queue once done with that level move to next level 
            level=[]
            while len(q)!=0:
                node=q.pop()
                level.append(node.val)
                
                if(node.left):
                    nq.appendleft(node.left)
                if(node.right):
                    nq.appendleft(node.right)
            traversal.append(level)
            q=nq
        return traversal
