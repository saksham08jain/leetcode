# Last updated: 11/11/2025, 09:42:24
class TrieNode:
    def __init__(self,char='',children=None):
        # self.char=char 
        if not children:
            children={}
        self.children=children
class Trie:

    def __init__(self):
        self.root=TrieNode()
        #this dictionraty maps each character to another trieNode
        

    def insert(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.children['X']=None
            


        

    def search(self, word: str) -> bool:
        cur=self.root
        for c in word: 
            if c not in cur.children:
                return False 
            cur=cur.children[c]
        return 'X' in cur.children

        

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for c in prefix: 
            if c not in cur.children:
                return False 
            cur=cur.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)