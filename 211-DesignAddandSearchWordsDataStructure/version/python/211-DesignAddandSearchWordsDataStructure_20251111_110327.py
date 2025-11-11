# Last updated: 11/11/2025, 11:03:27
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        #atmost two dots ... 
        #maintain a list of all possibilites 
        #since max 26 chars each lebel 
        #max 26^2 possibilities 
        #TC O(word length + 676)
        # print('searching for ',word)
        cur_pos=[self.root] #string , current node 

        for c in word: 
            # print(cur_pos,c)
            new_pos=[]
            if c!='.':
                for prev_node in cur_pos: 
                    #kepp only those possibilities which match this c as next word 
                    if c in prev_node.children:
                        new_node=prev_node.children[c]
                        new_pos.append(new_node)
                
                
                
            else:
                
                    for prev_node in cur_pos:
                        for nextt in prev_node.children:
                            new_pos.append(prev_node.children[nextt])
            cur_pos=new_pos
        #if any of cur_pos is a Word return True 
        for node in cur_pos:
            if node.word:
                return True 
        return False
                



        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)