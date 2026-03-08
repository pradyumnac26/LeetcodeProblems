class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        s = set(wordList) 
        q = deque([(beginWord, 1)]) 
        if endWord not in s : 
            return 0
        while q : 
            word, dist = q.popleft() 
            if word == endWord : 
                return dist 
            for i in range(len(word)): 
                for ch in "abcdefghijklmnopqrstuvwxyz" : 
                    newWord = word[:i] + ch + word[i+1:] 
                    if newWord in s : 
                        q.append((newWord, dist+1)) 
                        s.remove(newWord)
        return 0






            



        