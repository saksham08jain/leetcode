# Last updated: 5/6/2025, 11:08:41 pm
class Trie:

    def __init__(self):
        self.head={}#this dict will store the children

    def insert(self, word: str) -> None:
        word+='.'
        cur=self.head
        for char in word:
            if char in cur:
                cur=cur[char]
            else:
                cur[char]={}
                cur=cur[char]
        #cur[char]={}
        #print(cur)
        #print(self.head)

    def search(self, word: str) -> bool:
        cur=self.head
        for char in word:
            if char not in cur:
                return False 
            cur=cur[char]
        #print('Seacrhed cur',cur)
        if '.' in cur:
            return True 
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        cur=self.head
        for char in prefix:
            if char not in cur:
                return False 
            cur=cur[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)