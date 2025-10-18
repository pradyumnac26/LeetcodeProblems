class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        s = set(wordList)
        q = deque([(beginWord, 1)])
        s.discard(beginWord)
        if endWord not in s:
            return 0
        while q : 
            word, steps = q.popleft() 
            if word == endWord : 
                return steps
            for i in range(len(word)): 
                tochange = word[i] 
                for ch in "abcdefghijklmnopqrstuvwxyz" : 
                    new_word = word[:i] + ch + word[i+1:]
                    if new_word in s : 
                        s.remove(new_word) 
                        q.append((new_word, steps+1))
        return 0



        
        