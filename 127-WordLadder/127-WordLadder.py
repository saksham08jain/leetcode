# Last updated: 5/6/2025, 11:09:28 pm
from typing import *
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        
        sett=set(wordList)
    
        q=deque()
        q.append((beginWord,1))
        #sett.remove(beginWord)
        while len(q)!=0:
            cur_word,steps=q.popleft()
            if cur_word==endWord:
                return steps
            alpha='abcdefghijklmnopqrstuvwxyz'
            for i in range(len(cur_word)):
                for j in alpha:
                    new_word=cur_word[:i]+j+cur_word[i+1:]
                    if new_word in sett:
                        q.append((new_word,steps+1))
                        sett.remove(new_word)
        return 0