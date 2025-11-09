# Last updated: 09/11/2025, 22:47:47
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    #i heard preorder is enough if you include null nodes 
    #lets see how , lets figure ts out 
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #do a preorder traversal marking nulls with X 
        ser=[]
        def pre(root):
            nonlocal ser
            if not root:
                ser.append('X')
                return
            ser.append(str(root.val)+',')
            pre(root.left)
            pre(root.right)
        pre(root)
        print('ser',''.join(ser))
        return ''.join(ser)
    def extract_num_and_get_ptr(self,data,startPtr):
        newPtr=startPtr
        num=[]
        while data[newPtr]!=',':
            num.append(data[newPtr])
            newPtr+=1
        num=int(''.join(num))
        print(num,startPtr,newPtr)
        return num,newPtr

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #instead of doing this for negative numbers i could also do thats string till first x defines offset much cleaner much more scalable 
        #alos the edge cases feel lcunky but yeah 
        #oh f negative numbers and multiple digit numbers i didnt think of ahhh shooot shooot 
        #mehh okay lets end each number with a , 
        ptr=0
        if data[0]=='X':
            return None 
        val,ptr=self.extract_num_and_get_ptr(data,ptr)

        root=TreeNode(int(val))#int not needed , artifact of old code 
        stack=[[root,True]]
        #node,is it turning right or left 
        #True means left and is teh default since root left right 
        ptr+=1
        while ptr<len(data):
            #why i am doing manual stakc instead of recusrion idk tbh but lets goo 
            nextt=data[ptr]
            
            if nextt=='X':
                #if you were going left now start going right 
                if stack[-1][1]:
                    stack[-1][1]=False
                #if you were going right 
                #then this noode is done
                else: 
                    while stack and stack[-1][1]==False:
                        stack.pop()
                    if stack:
                        stack[-1][1]=False
            else:
                val,ptr=self.extract_num_and_get_ptr(data,ptr)
                cur,dirr=stack[-1]
                if dirr:
                    cur.left=TreeNode(val)
                    stack.append([cur.left,True])
                else:
                    cur.right=TreeNode(val)
                    stack.append([cur.right,True])
            ptr+=1
        return root


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))