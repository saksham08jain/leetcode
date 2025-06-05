# Last updated: 5/6/2025, 11:07:08 pm
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = ''

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.longest_word = ''

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.word = word

    def find_longest_word(self) -> str:
        self.dfs(self.root)
        return self.longest_word

    def dfs(self, node: TrieNode) -> None:
        for char, child in node.children.items():
            if child.is_end:
                if len(child.word) > len(self.longest_word) or (len(child.word) == len(self.longest_word) and child.word < self.longest_word):
                    self.longest_word = child.word
                self.dfs(child)

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie.find_longest_word()