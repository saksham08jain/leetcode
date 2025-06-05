# Last updated: 5/6/2025, 11:09:45 pm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        queue=deque()
        queue.append(root)
        ans=[]
        level=1
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
                
                #children=children[::-1] # doesnt work cause order in queue changes so 
            #print(children)
            level+=1
            for child in children:
                queue.append(child)
            if level&1:
                arr=arr[::-1]
            ans.append(arr)
        #print(ans)
        return ans