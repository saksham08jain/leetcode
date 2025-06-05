# Last updated: 5/6/2025, 11:09:46 pm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        queue=deque()
        queue.append(root)
        ans=[]
        while len(queue)!=0:
            arr=[]
            children=[]
            while len(queue)!=0:
                cur=queue.popleft()
                
                #print(cur.val,end=' ')
                arr.append(cur.val)
                if cur.left:
                    children.append(cur.left)
                if cur.right:
                    children.append(cur.right)
            #print(children)
            for child in children:
                queue.append(child)
            ans.append(arr)
        #print(ans)
        return ans