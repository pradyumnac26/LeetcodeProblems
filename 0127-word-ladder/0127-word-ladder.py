class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # a transformation seq from word beginWord to endWord using wordList , 
        if endWord not in wordList : 
            return 0 
        s = set(wordList) 
        q = deque([(beginWord, 1)])
        while q : 
            word, dist = q.popleft() 
            if word == endWord : 
                return dist
            for i in range(len(word)): 
                for j in "abcdefghijklmnopqrstuvwxyz" : 
                    new_word = word[:i] + j + word[i+1:]  
                    if new_word in s : 
                        q.append((new_word, dist+1)) 
                        s.remove(new_word)
        return 0
        
        
        